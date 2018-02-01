#!/bin/bash

pip install -r requirements.txt
sudo PYTHONPATH="`pwd`/src:`pwd`"
cd src
python main.py