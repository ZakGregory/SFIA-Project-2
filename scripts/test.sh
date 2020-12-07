#! /bin/bash

sudo apt install python3-pip python3-venv -y

python3 -m venv venv
. venv/bin/activate
pip3 install flask flask-testing pytest pytest-cov requests Werkzeug==0.16.1

pytest ./service1 
pytest ./service2
pytest ./service3
pytest ./service4

deactivate
