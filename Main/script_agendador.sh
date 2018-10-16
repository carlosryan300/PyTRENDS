#!/bin/bash
cd ..
source bin/activate
echo $(python --version)
cd Agendador
python script_agendador.py
deactivate
