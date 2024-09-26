#!/bin/bash

PORT=3001

if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null; then
    echo "Error: Port $PORT is already in use."
    exit 1
fi

nohup python notify_service.py >> /tmp/notify_service.log 2>&1 &
