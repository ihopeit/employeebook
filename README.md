## 构建镜像
构建之前登陆 docker hub

  * docker login
  * docker build  -t ihopeit/employeebook-base:0.8 .


交互运行:

* docker run -it --rm -p 8000:8000 --entrypoint /bin/sh ihopeit/employeebook-base:0.8

## 使用镜像快速搭建开发环境
场景/问题：
* 开发阶段，代码频繁改动，每次改动重新打镜像效率低，希望代码改动可以直接在运行的容器中体现出来。


解决方案： 
* 开发环境， 指定本地源码目录
* docker run -it --rm -p 8000:8000 -v "$(pwd)":/data/employeebook ihopeit/employeebook-base:0.8

指定加载源码 && 环境变量：

* docker run --rm -p 8000:8000 -v "$(pwd)":/data/employeebook --env server_params="--settings=employeebook.localSettings" ihopeit/employeebook-base:0.8