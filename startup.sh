#!/bin/bash
git clone https://github.com/j-dax/simple-flask-jenkins

cd simple-flask-jenkins
pip3 install pipenv
python3 -m pipenv install -r requirements.txt
python3 -m pipenv run python3 src/app.py &> flask.log
