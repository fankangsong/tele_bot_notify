#!/bin/bash

pid=$(pgrep -f notify_service.py)

if [ -z "$pid" ]; then
    echo "没有找到 notify_service.py 进程"
else
    echo "找到 notify_service.py 进程，PID: $pid"
    echo "正在结束进程..."
    kill $pid
    
    # 检查进程是否已经结束
    if ps -p $pid > /dev/null; then
        echo "进程未能正常结束，尝试强制结束..."
        kill -9 $pid
    else
        echo "进程已成功结束"
    fi
fi
