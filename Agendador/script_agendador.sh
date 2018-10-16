#!/bin/bash
cd ..
source bin/activate
cd Agendador
echo $(python --version)
python script_agendador.py
deactivate
