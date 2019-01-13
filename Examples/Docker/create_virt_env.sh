#! /bin/bash

python -m venv virtenv

source virtenv/bin/activate

git clone https://github.com/codytrey/ModemStatus.git

cd ModemStatus

pip install --upgrade pip

pip install .

pip install -r requirements.txt