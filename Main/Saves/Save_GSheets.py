import os, pandas as pd, time
import gspread, json
from oauth2client.service_account import ServiceAccountCredentials as OSS
from Validation.Method.Connection_Network import Valida_Connection
from Saves.Save_Csv import j
i = 1

PATH = os.getcwd()
def SetValuesGSheets(NameTable, ListValue):
    print("SetValuesGSheets") 
    try:
        VAR_GOOGLE =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        CREDENCIAIS = OSS.from_json_keyfile_name(PATH+'/FILES/JS/bot_whp.json', VAR_GOOGLE)
        AUTORIZA = gspread.authorize(CREDENCIAIS) 
        Sheet = AUTORIZA.open(NameTable).sheet1
        Valida_Connection()
        Sheet.append_row(ListValue)
    except Exception as Erro:
        print(Erro)
        pass
def PrepareList(NameTable, ListValue, ColumnOne, KeyWord, self):
    print("PrepareList") 
    df_Values = PrepareValue(ListValue, ColumnOne, KeyWord, self)
    df_InsertSheets = pd.DataFrame(df_Values)
    for index,Reads in df_InsertSheets.iterrows():
        SetValuesGSheets(NameTable, list(Reads))
def PrepareListOverTime(self, ListValue):
    print("PrepareListOverTime") 
    df_InsertSheets = pd.DataFrame(ListValue)
    for index,Reads in df_InsertSheets.iterrows():
        SetValuesGSheets(self, list(Reads))
def PrepareValue(List, ColumnOne, KeyWord, self):
    print("PrepareValue") 
    global i
    Time = time.strftime("%d/%m/%Y %H:%M")
    ListData = {
        '{0}'.format(ColumnOne):[],
        'values':[],
        'Termo Buscado':[],
        'Data de Extração':[],
        'Palavra Pivo':[],
        'Num da Comp':[],
        'Periodo':[]
    }
    ListValue = pd.DataFrame(List)
    for KWords in KeyWord:
        for index,Reads in ListValue.iterrows():
            ListData['{0}'.format(ColumnOne)].append(Reads[ColumnOne])
            ListData['values'].append(Reads[KWords])
            ListData['Termo Buscado'].append(KWords)
            ListData['Data de Extração'].append(Time)
            ListData['Palavra Pivo'].append(KeyWord[0])
            ListData['Num da Comp'].append("{0}º Comparação".format(i))
            ListData['Periodo'].append(self)
    i = i+1
    return ListData
def GSheet():
    print('GSheet')
    Valida_Connection()
    escopo =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credenciais =OSS.from_json_keyfile_name(PATH+'/FILES/JS/bot_whp.json', escopo)
    autorizacao = gspread.authorize(credenciais)
    sheets = autorizacao.open("rotinas").worksheet("Trends_Rotinas")
    Person = str(sheets.acell('B6').value) +' '+ str(sheets.acell('B7').value)
    Rotina = {
        'perio':sheets.acell('A2').value,
        'opcao':sheets.acell('B2').value,
        'salva':sheets.acell('C2').value,
        'perso':Person
    }
    return Rotina  
def Sitution(Value):
    escopo = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(PATH+"/json/bot_whp.json", escopo)
    autorizacao = gspread.authorize(credenciais)
    sheet = autorizacao.open('rotinas').worksheet('Trends_Rotinas')
    sheet.update_acell('G4', Value)
def ZerarI():
    global i
    i = 1
    j = 1


# Crie seu arquivo json de API
# Abra o arquivo e procuro o campo 'client_email':
# Copie o e-mail
# Vá no Sheets e clique em compartilhar sheets e adicione o e-mail para editar
# Rode o Script
from oauth2client.service_account import  ServiceAccountCredentials
import gspread
import pandas

def GoogleSheets(ArrayOf):
    # Nome da tabela edite confome o que precise 
    NomeTable = 'Nome_da_tabela'
    # Nome da aba da tabela edite confome o que precise
    AbaSheet = 'Nome_da_Aba'
    # Deixe na mesma pasta o arquivo json de API
    NameJson = '/nome_do_arquivo_json.json'
    # Variavél com Local onde está o arquivo, não precisa editar.
    PATH_NAME = os.getcwd()+NameJson
    # lista com as altorizações google, local onde encontrasse as tabelas, não precisa editar.
    VAR_GOOGLE =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    # autenticando com os serviços do google, não precisa alterar
    CREDENCIAIS = ServiceAccountCredentials.from_json_keyfile_name(PATH_NAME, VAR_GOOGLE)
    # autorizando autenticação do google
    AUTORIZA = gspread.authorize(CREDENCIAIS)
    # selecionando a tabela e aba que desejo setar as infomações
    GETTABLE = AUTORIZA.open(NomeTable).worksheet(AbaSheet)
    # setando as informações
    GETTABLE.append_row(ArrayOf)

def ReadCSV(FileName):
    # Ler Arquivo
    read = pandas.read_csv(FileName)
    # Convertendo dados para dataframe para facilitar a inserção.
    df_data = pandas.DataFrame(read)
    # Laço responsável por setar as informações no google sheets.
    for index, linhas in df_data.iterrows():
        # Chamando o função de inserir dados no sheets e passando os dados.
        GoogleSheets(linhas)

ReadCSV('Nome_do_CSV')