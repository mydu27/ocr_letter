# 基于的基础镜像
FROM python:3.7.4

# 复制代码文件到容器
COPY . /home/ocr_server/

# 设置代码工作目录
WORKDIR /home/ocr_server

# 将容器内的UTC时间更改为CST时间
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone

# 更新apt-get库
RUN apt-get update

# 安装vim
RUN apt-get install -y vim

# 安装ocr识别库
RUN apt install tesseract-ocr -y

# 安装项目依赖文件到容器
RUN pip install --no-cache-dir -r /home/ocr_server/requirements.txt


#运行启动文件
ENTRYPOINT ["python", "/home/ocr_server/runserver.py"]