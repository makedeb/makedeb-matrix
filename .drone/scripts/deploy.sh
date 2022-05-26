#!/usr/bin/env bash
set -eu

deploy_dir='/var/www/apps/makedeb-matrix'

# Create dir.
if ! [[ -d "${deploy_dir}" ]]; then
    mkdir -p "${deploy_dir}"
fi

# Stop current services.
cd "${deploy_dir}"

if [[ -f './service.sh' ]]; then
    ./service.sh stop
fi

# Delete files of current deployed service.
find ./ -mindepth 1 -maxdepth 1 -exec rm -rf '{}' +

# Copy files for new deployment.
cd -
find ./ -mindepth 1 -maxdepth 1 -exec cp -R '{}' "${deploy_dir}/{}" \;


cd "${deploy_dir}"
./service.sh start

# vim: set sw=4 expandtab:
