#! /bin/bash

pip3 install -r service1/requirements.txt
pytest ./service1 
pytest ./service2
pytest ./service3
pytest ./service4
