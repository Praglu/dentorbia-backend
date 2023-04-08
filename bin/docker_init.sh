#!/bin/sh

set -e

cp -n envs/docker-env-default envs/.docker.env

docker-compose build
docker-compose up --no-start
