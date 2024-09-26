# 使用官方 Python 基础镜像
FROM python:3.11-slim 

# 设置工作目录
WORKDIR /app

# 将当前目录下的 Python 脚本和可能的 send.html 文件复制到容器内的工作目录
COPY index.py form.html /app/ 

# 安装依赖（如果你的 Python 脚本需要安装特定的 Python 库，可以在这里添加安装命令）
# RUN pip install -r requirements.txt

# 暴露容器内的端口，这个端口应该与 Python 脚本中使用的端口一致
EXPOSE ${PORT}

# 运行容器时设置环境变量并执行 Python 脚本
CMD ["python", "/app/index.py"]
