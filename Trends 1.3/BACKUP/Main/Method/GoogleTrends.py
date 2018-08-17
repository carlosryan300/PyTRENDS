import os, gspread, csv, sys, time, os.path as path
from oauth2client.service_account import ServiceAccountCredentials as OSS
from Validation.Method.Connection_Network import Valida_Connection
from Validation.Method.List_KeyWord import List_KeyWords, NumberKey, ListKeyWordsException
from Saves.Save_BigQuery import Save_BigQuery
from Saves.Save_Csv import Save_Csv
from pytrends.request import TrendReq
from openpyxl.workbook import Workbook
PATH = os.getcwd()
URLCONFIAVEIS= ['www.google.com', 'www.yahoo.com', "www.uol.com"]
VAR_GOOGLE =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
#CREDENCIAIS = OSS.from_json_keyfile_name('{0}/FILES/JS/bot_whp.json'.format(PATH), VAR_GOOGLE)

#AUTORIZA = gspread.authorize(CREDENCIAIS)
class GoogleTrends():
    def __init__():
        pass
    def NewByRegion(self):
        global PATH
        Local = "{0}/FILES/Excel/ByRegion.xlsx".format(PATH)
        NewFile = "{0}/FILES/Excel/By_Region.xlsx".format(PATH)
        i = 1
        try:
            Repeat = NumberKey()
            while i <= Repeat:
                KeyWords = List_KeyWords()
                print(KeyWords)
                if KeyWords != "" or KeyWords!=None:
                    pytrend = TrendReq(hl='pt-BR', geo='BR')
                    Valida_Connection()
                    pytrend.build_payload(kw_list=KeyWords,timeframe=self, geo="BR")
                    interest_by_region_df = pytrend.interest_by_region()
                    interest_by_region_df.to_excel(Local)
                    i = i + 1
                    #Save_BigQuery(KeyWords, "By_Region.xlsx", "geoName", self)
                    Save_Csv.Create_List(Local, 'geoName', 'values', NewFile, KeyWords)
            os.remove(Local)
        except Exception as Erro:
            print("def New_By_Region -> Ocorreu o Erro:{0}".format(Erro))
    def NewOverTime(self):
        i = 1
        try:
            Repeat = NumberKey()
            while i <= Repeat:
                KeyWords = List_KeyWords()
                print(KeyWords)
                if KeyWords != "":
                    pytrend = TrendReq(hl='pt-BR', geo='BR')
                    Valida_Connection()
                    pytrend.build_payload(kw_list=KeyWords,timeframe=self, geo="BR")
                    interest_over_time_df = pytrend.interest_over_time()
                    interest_over_time_df.to_excel("{0}/FILES/Excel/Over_Time.xlsx".format(PATH))
                    i = i + 1
                    Save_BigQuery(KeyWords, "Over_Time.xlsx", "date", self)
                    KeyWords.clear()
        except Exception as Erro:
            print("def New_Over_Time -> Ocorreu o Erro:{0}".format(Erro))  
    def NewRelatedQueries(self):
        i = 0
        try:
            pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR')    
            PalavraChave = ListKeyWordsException()
            REPEAT = 0
            ENCODING = "utf-8"
            COUNT = 0
            SAVE = []
            DATA_HORA = time.strftime("%d/%m/%y %H:%M")
            PATH_RISING = '{0}/FILES/Excel/CONSULTAS_RELACIONAS.csv'.format(PATH)
            PATH_TOP = '{0}/FILES/Excel/PRINCIPAIS_ASSUNTOS.csv'.format(PATH)
            PATH_TXT = "{0}/FILES/TXT/Top_Rising.txt".format(PATH)
            while REPEAT < len(PalavraChave):  
                Valida_Connection()
                QueryString = str(PalavraChave[REPEAT]) 
                pytrend.build_payload(kw_list=[QueryString],timeframe=self, geo="BR")
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
                    print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM CONSULTA RELACIONADA\n".format(QueryString))
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
                                    wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), self])
                                    f.close()
                            else:
                                with open(PATH_TOP, 'a', newline="", encoding=ENCODING) as f:
                                    wt = csv.writer(f, delimiter=";")     
                                    wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), self])
                                    f.close() 
                            COUNT = COUNT+1

                            sheet =  AUTORIZA.open("PRINCIPAIS_ASSUNTOS").sheet1
                            sheet.append_row([posicao, query.upper(), int(valor), DATA_HORA,QueryString.upper(), self])
                        else:
                            if path.isfile(PATH_RISING)==False:
                                with open(PATH_RISING, 'a', newline="", encoding=ENCODING) as f:
                                    wt = csv.writer(f, delimiter=";")   
                                    wt.writerow(["RISING","BUSCAS","VALOR","DATA E HORA","QUERY", "PERÍODO"])  
                                    wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), self])
                                    f.close()
                            else:
                                with open(PATH_RISING, 'a', newline="", encoding=ENCODING) as f:
                                    wt = csv.writer(f, delimiter=";")     
                                    wt.writerow([posicao, query.upper(), valor, DATA_HORA,QueryString.upper(), self])
                                    f.close()
                            time.sleep(1)
                            sheet =  AUTORIZA.open("CONSULTAS_RELACIONAS").sheet1
                            sheet.append_row([posicao, query.upper(), valor, DATA_HORA, QueryString.upper(), self])
                            COUNT = COUNT+1
                    SAVE.clear()
                    REPEAT = REPEAT+1
                    COUNT = 0
            print(".................TESTE << TOP AND RESING >> FINALIZADO.................\n")
        except Exception as Erro:
            print("def NewRelatedQueries Erro:{0}".format(Erro))
