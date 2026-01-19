#!/bin/bash

COMMIT="local-run"

# SINGLE-STAGE BUILD
START=$(date +%s)
docker build -f Dockerfile.single -t app-single .
END=$(date +%s)
SINGLE_TIME=$((END - START))

curl -X POST http://localhost:9000/metrics \
-H "Content-Type: application/json" \
-d "{\"commit_id\":\"$COMMIT\",\"build_type\":\"single\",\"build_time_seconds\":$SINGLE_TIME}"

# MULTI-STAGE BUILD
START=$(date +%s)
docker build -f Dockerfile.multi -t app-multi .
END=$(date +%s)
MULTI_TIME=$((END - START))

curl -X POST http://localhost:9000/metrics \
-H "Content-Type: application/json" \
-d "{\"commit_id\":\"$COMMIT\",\"build_type\":\"multi\",\"build_time_seconds\":$MULTI_TIME}"
