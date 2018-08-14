import os, pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials as OSS

def SetValuesGSheets(self, ListValue):
    PATH = "C:\\PROJECTS\\TRENDS\\Main\\Method"
    
    VAR_GOOGLE =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    CREDENCIAIS = OSS.from_json_keyfile_name('{0}/FILES/JS/bot_whp.json'.format(PATH), VAR_GOOGLE)
    AUTORIZA = gspread.authorize(CREDENCIAIS)
    
    Sheet = AUTORIZA.open(self).sheet1

    Sheet.append_row([])

def PrepareList():
    Values = (pd.read_excel("C:\\PROJECTS\\TRENDS\\Main\\Method\\FILES\\Excel\\By_Region.xlsx"))
    List = list(Values)
    Dict = dict(Values)

    print(len(List))
    print(len(Dict['Palavra Pivo']))
    
    #print(Dict)

PrepareList()