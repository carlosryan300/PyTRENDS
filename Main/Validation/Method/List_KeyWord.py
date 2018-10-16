import os, gspread, pandas
from oauth2client.service_account import ServiceAccountCredentials 
PATH = os.getcwd()
Regulador = 1
Implementador = 1
def List_KeyWords():
    global Implementador
    global Regulador
    Lista = KeyWords()
    Pivo = Lista[0] 
    if len(Lista)==1:
        print('SÓ EXISTE UMA PALAVRA, O TESTE EXECULTARÁ SEM COMPARAR OUTRAS PALAVRAS')
        PlayLoad = [Pivo]
        return PlayLoad
    while Implementador < len(Lista):
        PlayLoad = [Pivo]
        j = 1
        if len(Lista)<=4:
            for foin in range(Implementador, len(Lista)):
                PlayLoad.append(Lista[Implementador])
                Implementador = Implementador + 1
            return PlayLoad
        elif (Regulador) <= (len(Lista)//4): #valor padrão 4
            while j < 5: #valor padrão 5
                PlayLoad.append(Lista[Implementador])
                Implementador = Implementador + 1
                j = j + 1
            Regulador = Regulador+1
            return PlayLoad
        else:
            while Implementador < len(Lista):
                PlayLoad.append(Lista[Implementador])
                Implementador=Implementador+1
            return PlayLoad            
def ListKeyWordsException():
    Lista = KeyWords()
    return Lista
def NumberKey():
    Lista = KeyWords()
    Fastest = int((len(Lista)-1)%2)
    if len(Lista) <= 4:
        Retorno = 1
    elif Fastest==0:
        Retorno = int(len(Lista)-1)//4
    else:
        Retorno = int(len(Lista)-1)//4+1
    return Retorno
def KeyWords():
    escopo = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(PATH+'/FILES/JS/bot_whp.json', escopo)
    autorizacao = gspread.authorize(credenciais)
    sheets = autorizacao.open("rotinas").worksheet('Trends_Palavras')
    dados = sheets.get_all_records()
    KeyWords = pandas.DataFrame(dados)
    return list(KeyWords['Key_Words'])
def RegAndImp():
    global Implementador
    global Regulador
    Implementador = 1
    Regulador = 1
