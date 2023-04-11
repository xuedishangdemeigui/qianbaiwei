#! /bin/bash

APP_NAME=src/main

# setup env
python3 -m venv venv
source venv/bin/activate
type pip
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# start app
flask --app ${APP_NAME} run --host 0.0.0.0
