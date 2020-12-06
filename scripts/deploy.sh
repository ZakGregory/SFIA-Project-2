#! /bin/bash

ssh zgregory@swarm-manager << EOF
sudo docker pull zakgregory/practical-project-service1
sudo docker pull zakgregory/practical-project-service1
sudo docker pull zakgregory/practical-project-service1
sudo docker pull zakgregory/practical-project-service1

git clone https://github.com/ZakGregory/Practical-Project-Repo.git

sudo docker stack deploy --compose-file docker-compose.yml app
EOF
