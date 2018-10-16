from Validation.Method.Connection_Network import Valida_Connection
import os, time, sys, gspread
from GoogleTrends import GoogleTrends
from oauth2client.service_account import ServiceAccountCredentials
from Saves.Save_GSheets import GSheet, Sitution

PATH = os.getcwd()

def Report_Option(): 
    print("Report_Option")         
    os.makedirs("{0}/FILES/Excel/".format(PATH),exist_ok=True)
    opcao = GSheet()

    SalvarComo = {'CSV':1, 'Sheets':2, 'Ambos':3}
    Periodo = {
        'Última_Hora':'now 1-H',    'Últimas_Sete_Horas':'now 1-d', 'Últimos_Sete_Dias':'now 7-d',  'Último_Um_Mês':'today 1-m',
        'Últimos_Três_Meses':'today 3-m',   'Últimos_Cinco_Anos':'today 5-y',   'Todos_Os_Períodos':'all',  'Personalizado':''
    }
    
    Date = Periodo[str(opcao['perio']).replace(' ', '_')]
    ModeSave = SalvarComo[opcao['salva']]

    if opcao['perio'] == 'Personalizado':
        Date = opcao['perso']

    if opcao['opcao'] == 'Consultas Relacionadas': 
        
        GoogleTrends.NewRelatedQueries(Date, ModeSave)              

    elif opcao['opcao'] == 'Assuntos Relacionados':
        
        GoogleTrends.NewRelatedTopics(Date, ModeSave)

    elif opcao['opcao'] == 'Interesse Por Tempo':

        GoogleTrends.NewOverTime(Date, ModeSave)

    elif opcao['opcao'] == 'Interesse Por Região':
        
        GoogleTrends.NewByRegion(Date, ModeSave)

    elif opcao['opcao'] == 'Todas Anteriores':
        GoogleTrends.NewOverTime(Date, ModeSave)
        GoogleTrends.NewByRegion(Date, ModeSave)
        GoogleTrends.NewRelatedTopics(Date, ModeSave)
        GoogleTrends.NewRelatedQueries(Date, ModeSave) 
    Sitution(str(time.strftime('%Y-%m-%d %H:%M:%S')))
try:
    Report_Option() 
except Exception as Error:
    print(Error)
   
