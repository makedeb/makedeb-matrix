#!/usr/bin/bash
set -ex

# Set up config file.
sed -i "s|your-access-token|${makedeb_matrix_api_token}|" src/config.yaml

# Make sure needed directories exist.
cd /var/www/apps/makedeb-matrix/

if ! [[ -d ./data/makedeb-matrix/ ]]; then
	mkdir ./data/makedeb-matrix/ -p
fi

# Copy config to deployment directory.
cd -
cp src/config.yaml /var/www/apps/makedeb-matrix/data/config.yaml

# Bring up containers.
cp docker-compose.yml /var/www/apps/makedeb-matrix/docker-compose.yml

cd /var/www/apps/makedeb-matrix/
docker-compose up -d
