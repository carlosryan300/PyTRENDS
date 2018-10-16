#!/bin/bash
cd ..
source bin/activate
cd Main
echo $(python --version)
python Option.py
deactivate
