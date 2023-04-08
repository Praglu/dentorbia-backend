#!/bin/sh

set -e

docker-compose stop
docker-compose rm -svf
docker volume list | grep 'dentorbia-backend.+data' | awk '{ print $2 }' | xargs docker volume rm
docker images | egrep 'dentorbia-backend_.+' | awk '{ print $1 }' | xargs docker rmi -f
rm envs/.docker.env
