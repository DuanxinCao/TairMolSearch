# TairMosearch molview client

1. 参考开源 molview https://github.com/molview/molview.git
2. 创建molview 镜像  docker build -f Dockerfile -t tail-molview:1.0.0  .
3. 启动molview 服务  docker run -td -p 8001:80 -e API_URL=http://$MOLSEARCH_SERVER:$MOLSEARCH_PORT tail-molview:1.0.0
4. 浏览器访问  127.0.0.1:8001