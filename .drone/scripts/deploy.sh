#!/usr/bin/bash
set -ex

# Set up config file.
sed -i "s|your-access-token|${makedeb_matrix_api_token}|" src/config.yaml

# Make sure needed directories exist.
cd /var/www/apps/

if ! [[ -d ./data/makedeb-matrix/ ]]; then
	mkdir ./data/makedeb-matrix/ -p
fi

# Copy config to deployment directory.
cd -
cp src/config.yaml /var/www/apps/data/makedeb-matrix/config.yaml

# Bring up containers.
cp docker-compose.yml /var/www/apps/docker-compose.makedeb-matrix.yml

cd /var/www/apps/
docker-compose -f docker-compose.makedeb-matrix.yml up -d
