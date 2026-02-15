```md
# Layer-Optimized FastAPI Microservice Framework with CI Build Time Analytics

This project demonstrates how **Docker layer optimization and multi-stage builds** can significantly reduce CI build time.  
It also includes a **CI build-time analytics microservice** that stores and visualizes build metrics using MongoDB and FastAPI.


docker-compose down

docker system prune -af
docker builder prune -af

docker ps -a
docker images

docker-compose up --build

and in gitbash

cd service_app
bash ../ci-build.sh

docker-compose down at the end


## 🚀 Key Features

- Single-stage vs Multi-stage Docker builds
- Docker layer caching optimization
- CI build-time measurement
- MongoDB-backed analytics
- FastAPI microservices
- HTML dashboard for comparison
- Fully **Windows + VS Code + PowerShell compatible**



## 🧱 Project Architecture

```

layer-optimized-fastapi/
│
├── service_app/                # Application being built
│   ├── app/
│   ├── Dockerfile.single
│   ├── Dockerfile.multi
│   └── requirements.txt
│
├── analytics_service/          # CI build analytics service
│   ├── app/
│   ├── Dockerfile
│   └── requirements.txt
│
├── scripts/                    # PowerShell automation
│   ├── start.ps1
│   ├── stop.ps1
│   └── stop-clean.ps1
│
├── docker-compose.yml
└── README.md

```



## 🖥 Prerequisites (Windows)

- Windows 10 / 11  
- Docker Desktop (Linux containers enabled)  
- Visual Studio Code  
- PowerShell (default in VS Code)  

❌ Git Bash / WSL is **NOT required**



## ▶️ START THE PROJECT

### Step 1: Open VS Code
Open VS Code **in the project root directory**:

```

layer-optimized-fastapi

```



### Step 2: Open VS Code Terminal
Press:
```

Ctrl + `

````

Ensure terminal is **PowerShell**.



### Step 3: Start Services
```powershell
.\scripts\start.ps1
````

This will:

* Build Docker images
* Start MongoDB
* Start Analytics FastAPI service
* Run containers in background



### Step 4: Open Dashboard

Open browser:

👉 **[http://localhost:9000](http://localhost:9000)**



## 🧪 RUN CI BUILD COMPARISON (Windows)

> This simulates CI builds and sends metrics to the analytics service.

### Step 1: Go to service_app

```powershell
cd service_app
```



### Step 2: Measure SINGLE-stage build

```powershell
$single = Measure-Command {
    docker build -f Dockerfile.single -t app-single .
}
```



### Step 3: Measure MULTI-stage build

```powershell
$multi = Measure-Command {
    docker build -f Dockerfile.multi -t app-multi .
}
```



### Step 4: Send metrics to Analytics Service

#### Send SINGLE-stage metric

```powershell
Invoke-RestMethod http://localhost:9000/metrics `
-Method POST `
-ContentType "application/json" `
-Body (@{
    commit_id = "local-run"
    build_type = "single"
    build_time_seconds = [int]$single.TotalSeconds
} | ConvertTo-Json)
```

#### Send MULTI-stage metric

```powershell
Invoke-RestMethod http://localhost:9000/metrics `
-Method POST `
-ContentType "application/json" `
-Body (@{
    commit_id = "local-run"
    build_type = "multi"
    build_time_seconds = [int]$multi.TotalSeconds
} | ConvertTo-Json)
```



### Step 5: View Results

Refresh browser:

👉 **[http://localhost:9000](http://localhost:9000)**

You will see:

* Average single-stage build time
* Average multi-stage build time
* Percentage improvement



## ⏹ STOP THE PROJECT (Safe – No Data Loss)

```powershell
.\scripts\stop.ps1
```

This will:

* Stop all containers
* Preserve MongoDB data
* Keep analytics history intact



## 🔁 RESTART SAFELY (Recommended)

```powershell
.\scripts\stop.ps1
.\scripts\start.ps1
```

✔ Containers restart
✔ MongoDB data preserved
✔ Dashboard history remains



## 🧹 DELETE EVERYTHING (FULL CLEANUP)

⚠️ **WARNING: This deletes ALL data including MongoDB analytics**

```powershell
.\scripts\stop-clean.ps1
```

Use this when:

* You want a fresh demo
* You want to reset analytics data
* You are starting from scratch



## 🔍 VERIFY STATUS

### Check running containers

```powershell
docker ps
```

### No containers running

```powershell
docker ps
# (empty output)
```



## 📊 Sample Result

```
Single-stage : 21.5 seconds
Multi-stage  : 10.0 seconds
Improvement  : 53.49%
```

This proves Docker layer optimization effectiveness.



## 🧠 Viva / Interview Explanation

> “This project demonstrates how isolating dependencies in Docker multi-stage builds enables layer caching, reducing CI build time by over 50%. Build metrics are collected and visualized using a FastAPI analytics microservice.”



## ✅ What This Project Proves

✔ Docker layer optimization
✔ Multi-stage build efficiency
✔ CI performance analytics
✔ Microservice architecture
✔ Windows DevOps workflow



## 📌 Author

**Sadula Rushidhar**
M.Tech – Computer Science & Engineering (AI & ML)



## 🚀 Future Enhancements

* GitHub Actions CI pipeline
* Build-time visualization charts
* Authentication for analytics service
* Kubernetes deployment


```



