from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .db import metrics
from .models import BuildMetric

app = FastAPI(title="CI Build Analytics")

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.post("/metrics")
def save_metric(metric: BuildMetric):
    metrics.insert_one(metric.dict())
    return {"status": "saved"}

@app.get("/compare")
def compare():
    single = list(metrics.find({"build_type": "single"}))
    multi = list(metrics.find({"build_type": "multi"}))

    if not single or not multi:
        return {"error": "Not enough data"}

    avg_single = sum(x["build_time_seconds"] for x in single) / len(single)
    avg_multi = sum(x["build_time_seconds"] for x in multi) / len(multi)
    improvement = ((avg_single - avg_multi) / avg_single) * 100

    return {
        "single": round(avg_single, 2),
        "multi": round(avg_multi, 2),
        "improvement": round(improvement, 2)
    }

@app.get("/")
def dashboard(request: Request):
    data = compare()
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "data": data}
    )
