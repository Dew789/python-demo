#!/usr/bin/bash

images=python-demo:1.0.0
docker stop python-demo && docker rm python-demo
docker rmi $images

docker build -t $images .

docker run \
    --restart=always \
    --log-opt max-size=10m \
    --net=host \
    --privileged=true  \
    --name python-demo \
    -p 6060:6060 \
    -v /etc/localtime:/etc/localtime \
    -d $images
