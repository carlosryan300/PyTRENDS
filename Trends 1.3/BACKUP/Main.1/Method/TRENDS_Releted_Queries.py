import gspread, csv, os, sys, time, os.path as path, pandas as pd
from oauth2client.service_account import ServiceAccountCredentials as OSS
from Validation.Method.Connection_Network import Check_Connection
from pytrends.request import TrendReq
from openpyxl.workbook import Workbook

PATH = os.getcwd()
ENCODING = "utf-8"
SAVE = []
DATA_HORA = time.strftime("%d/%m/%y %H:%M:%S")

def Related_Queries():
    pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR')  
    Date = "today 1-m"  
    PalavraChave = ["consul", "brastemp", "compra certa"]
    REPEAT = 0
    COUNT = 0
    PATH_RISING = '{0}/FILES/Excel/CONS_RELAC_EM_ASCENSAO.csv'.format(PATH)
    PATH_TOP = '{0}/FILES/Excel/CONS_RELAC_PRINCIPAIS.csv'.format(PATH)
    PATH_TXT = "{0}/FILES/TXT/Top_Rising.txt".format(PATH)
    while REPEAT < len(PalavraChave):  
    #PARTE 1
        if Check_Connection()==True:
            pass
        else:
            print("==================NÃO FOI POSSIVEL CONECTAR A INTERNET================\n")
        QueryString = str(PalavraChave[REPEAT]) 
        
        pytrend.build_payload(kw_list=[QueryString],timeframe=Date, geo="BR")
        
        #TOP AND RISING
        related_queries_dict = pytrend.related_queries()

        PrettyArq =  str(related_queries_dict.get(QueryString))
        with open(PATH_TXT, 'a', encoding=ENCODING, newline="") as Criar:
            Criar.write(PrettyArq.replace("{","").replace(":", "").replace("'top'","").replace("query","").replace("value","").replace("'","").replace("rising","").replace("}","").replace(",","").replace("None",""))
            Criar.close()

        with open(PATH_TXT, 'r', encoding=ENCODING, newline="") as abrir:
            for limpar in abrir:
                limpar = limpar.rstrip()
                if limpar !="":
                    SAVE.append(limpar)
            abrir.close()
            os.remove(PATH_TXT)

        if not SAVE:
            print("..A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM TOP E TENDÊNCIA..\n".format(QueryString))
            REPEAT = REPEAT+1
        else:
            for saves in SAVE:
                posicao = (saves[:2]).rstrip().lstrip()
                valor = (saves[int(len(saves)-6):]).rstrip().lstrip()     
                query = (saves[2:int(len(saves)-6)].strip().lstrip())
                if COUNT == int(posicao):
                    if path.isfile(PATH_TOP)==False:
                        with open(PATH_TOP, 'a', newline="", encoding=ENCODING) as f:
                            wt = csv.writer(f, delimiter=";")   
                            wt.writerow(["TOP","BUSCAS","VALOR","DATA E HORA","QUERY", "PERÍODO"]) 
                            wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), Date])
                            f.close()
                    else:
                        with open(PATH_TOP, 'a', newline="", encoding=ENCODING) as f:
                            wt = csv.writer(f, delimiter=";")     
                            wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), Date])
                            f.close() 
                    COUNT = COUNT+1

                    #sheet =  AUTORIZA.open("PRINCIPAIS_ASSUNTOS").sheet1
                    #sheet.append_row([posicao, query.upper(), int(valor), DATA_HORA,QueryString.upper(), Date])
                else:
                    if path.isfile(PATH_RISING)==False:
                        with open(PATH_RISING, 'a', newline="", encoding=ENCODING) as f:
                            wt = csv.writer(f, delimiter=";")   
                            wt.writerow(["RISING","BUSCAS","VALOR","DATA E HORA","QUERY", "PERÍODO"])  
                            wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), Date])
                            f.close()
                    else:
                        with open(PATH_RISING, 'a', newline="", encoding=ENCODING) as f:
                            wt = csv.writer(f, delimiter=";")     
                            wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), Date])
                            f.close()
                    time.sleep(1)
                    #sheet =  AUTORIZA.open("CONSULTAS_RELACIONAS").sheet1
                    #sheet.append_row([posicao, query.upper(), valor, DATA_HORA, QueryString.upper(), Date])
                    COUNT = COUNT+1
            SAVE.clear()
            REPEAT = REPEAT+1
            COUNT = 0
    print(".................TESTE << TOP AND RESING >> FINALIZADO.................\n")

Related_Queries()