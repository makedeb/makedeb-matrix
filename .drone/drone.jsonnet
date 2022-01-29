local buildAndPublish() = {
    name: "publish-and-deploy",
    kind: "pipeline",
    type: "docker",
    volumes: [
        {name: "docker", host: {path: "/var/run/docker.sock"}},
        {name: "docker-compose", host: {path: "/usr/bin/docker-compose"}},
        {name: "deploy-dir", host: {path: "/var/www/apps"}}
    ],
    steps: [
        {
            name: "publish",
            image: "ubuntu:20.04",
            volumes: [
                {name: "docker", path: "/var/run/docker.sock"},
                {name: "docker-compose", path: "/usr/bin/docker-compose"},
            ],
            environment: {proget_api_key: {from_secret: "proget_api_key"}},
            commands: [
                "apt update",
                "apt install docker.io -y",
                ".drone/scripts/publish.sh"
            ]
        },
        {
            name: "deploy",
            image: "ubuntu:20.04",
            volumes: [
                {name: "docker", path: "/var/run/docker.sock"},
                {name: "docker-compose", path: "/usr/bin/docker-compose"},
                {name: "deploy-dir", path: "/var/www/apps"}
            ],
            environment: {makedeb_matrix_api_token: {from_secret: "makedeb_matrix_api_token"}},
            commands: [
                "apt update",
                "apt install docker.io -y",
                ".drone/scripts/deploy.sh"
            ]
        }
    ]
};

[buildAndPublish()]

// vim: set syntax=typescript ts=4 sw=4 expandtab:
