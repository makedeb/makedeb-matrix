#!/usr/bin/bash
set -ex

docker login -u api -p "${proget_api_key}" "${proget_server}"
docker-compose build --no-cache
docker-compose push
