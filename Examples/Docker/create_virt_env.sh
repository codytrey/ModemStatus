#! /bin/bash

python -m venv virtenv

source virtenv/bin/activate

git clone https://github.com/codytrey/ModemStatus.git

cd ModemStatus

pip install .

cd

pip install -r ModemStatus/requirements.txt