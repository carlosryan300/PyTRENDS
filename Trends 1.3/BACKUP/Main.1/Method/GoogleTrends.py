import csv, os, os.path as path, sys, time, pandas as pd
from openpyxl.workbook import Workbook
from pytrends.request import TrendReq

from Saves.Save_BigQuery import Save_BigQuery
from Saves.Save_Csv import Save_Csv
from Saves.Save_GSheets import (PrepareList, PrepareListOverTime)
from Validation.Method.Connection_Network import Valida_Connection
from Validation.Method.List_KeyWord import (List_KeyWords,ListKeyWordsException, NumberKey)

PATH = os.getcwd()


class GoogleTrends():
    def __init__():
        pass
    def NewByRegion(self):
        global PATH
        Local = "{0}/FILES/Excel/ByRegion.csv".format(PATH)
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
                    interest_by_region_df.to_csv(Local)
                    df_dataFrame = pd.DataFrame(pd.read_csv(Local))
                    os.remove(Local)
                    Save_Csv.PrepareValue(df_dataFrame,'geoName', 'By_Region', KeyWords, self)
                    PrepareList('By_Region', df_dataFrame, "geoName",KeyWords, self)
                i = i + 1
            print(".................TESTE << BY REGION >> FINALIZADO.................\n")
        except Exception as Erro:
            print("def New_By_Region -> Ocorreu o Erro:{0}".format(Erro))
    def NewOverTime(self):
        global PATH
        Local = "{0}/FILES/Excel/OverTime.csv".format(PATH)
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
                    interest_over_time_df = pytrend.interest_over_time()
                    interest_over_time_df.to_csv(Local, decimal=',')
                    df_dataFrame = pd.DataFrame(pd.read_csv(Local))
                    os.remove(Local)
                    Save_Csv.PrepareValue(df_dataFrame, 'date', 'Over_Time', KeyWords, self)
                    PrepareList('Over_Time', df_dataFrame, 'date', KeyWords, self)
                i = i + 1
            print(".................TESTE << OVER TIME >> FINALIZADO.................\n")
        except Exception as Erro:
            print("def New_Over_Time -> Ocorreu o Erro:{0}".format(Erro))        
    def NewRelatedQueries(self):
        PATH_QUERY = '{0}/FILES/Excel/'.format(PATH)
        PalavraChave = ListKeyWordsException()
        Time = time.strftime("%d/%m/%Y %H:%M")
        try:
            pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR') 
            for i in range(0, len(PalavraChave)): 
                QueryString = str(PalavraChave[i]) 
                Valida_Connection()
                pytrend.build_payload(kw_list=[QueryString],timeframe=self, geo="BR")
                related_queries_dict = pytrend.related_queries()
                ListValue = {
                    'Top':[],
                    'Values':[],
                    'Consultas Relacionadas':[],
                    'Termo Buscado':[],
                    'Tipo':[],
                    'Data de Extração':[],
                    'Periodo':[]
                }
                LenInTop = len(list(related_queries_dict[QueryString]['top']["query"]))
                LenInRising = len(list(related_queries_dict[QueryString]['rising']["query"]))
                for i in (range(0, LenInTop)):
                    ListValue['Top'].append(i)
                    ListValue['Termo Buscado'].append(QueryString)
                    ListValue['Tipo'].append('Principais')
                    ListValue['Data de Extração'].append(Time)
                    ListValue['Periodo'].append(self)    
                for i in (range(0, LenInRising)):
                    ListValue['Top'].append(i)
                    ListValue['Termo Buscado'].append(QueryString)
                    ListValue['Tipo'].append('Em Ascensão')
                    ListValue['Data de Extração'].append(Time)
                    ListValue['Periodo'].append(self)  
                ListValue.update({'Consultas Relacionadas': list(related_queries_dict[QueryString]['top']["query"])+list(related_queries_dict[QueryString]['rising']["query"])})
                ListValue.update({'Values': list(related_queries_dict[QueryString]['top']["value"])+list(related_queries_dict[QueryString]['rising']["value"])})
                Save_Csv.SaveRelated(ListValue,'{0}/Consultas_Relacionada.csv'.format(PATH_QUERY))
                PrepareListOverTime('Related_Queries', ListValue)
                print(".................TESTE << BY REGION >> FINALIZADO.................\n")   
        except Exception as Erro:
            print("def NewRelatedQueries ->Ocorreo o Erro:{0}".format(Erro))

    def NewRelatedTopics(self):
        PATH_QUERY = '{0}/FILES/Excel/'.format(PATH)
        PalavraChave = ListKeyWordsException()
        Time = time.strftime("%d/%m/%Y %H:%M")
        try:
            pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR') 
            for i in range(0, len(PalavraChave)): 
                QueryString = str(PalavraChave[i]) 
                Valida_Connection()
                pytrend.build_payload(kw_list=[QueryString],timeframe=self, geo="BR")
                related_topcs_dict = pytrend.related_topics()
                ListValue = {
                    'Top':[],
                    'Assuntos Relacionadas':[],
                    'type':[],
                    'Values':[],
                    'Termo Buscado':[],
                    'Tipo':[],
                    'Data de Extração':[],
                    'Periodo':[]
                }
                LenInTop = len(list(related_topcs_dict[QueryString]['title']))
                for i in (range(0, LenInTop)):
                    ListValue['Top'].append(i)
                    ListValue['Termo Buscado'].append(QueryString)
                    ListValue['Tipo'].append('Principais')
                    ListValue['Data de Extração'].append(Time)
                    ListValue['Periodo'].append(self)    
                for i in (range(0, LenInRising)):
                    ListValue['Top'].append(i)
                    ListValue['Termo Buscado'].append(QueryString)
                    ListValue['Tipo'].append('Em Ascensão')
                    ListValue['Data de Extração'].append(Time)
                    ListValue['Periodo'].append(self)  
                ListValue.update({'Consultas Relacionadas': list(related_topcs_dict[QueryString]['top']["query"])+list(related_topcs_dict[QueryString]['rising']["query"])})
                ListValue.update({'Values': list(related_topcs_dict[QueryString]['top']["value"])+list(related_topcs_dict[QueryString]['rising']["value"])})
                Save_Csv.SaveRelated(ListValue,'{0}/Assunto_Relacionada.csv'.format(PATH_QUERY))
                PrepareListOverTime('Related_Queries', ListValue)
                print(".................TESTE << BY REGION >> FINALIZADO.................\n")   
        except Exception as Erro:
            print("def NewRelatedQueries ->Ocorreo o Erro:{0}".format(Erro))

# 
    
    #  def NewRelatedQueries(self):
    #     i = 0
    #     global ListValue
    #     try:
    #         pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR')    
    #         PalavraChave = ListKeyWordsException()
    #         REPEAT = 0
    #         COUNT = 0
    #         SAVE = []
    #         PATH_QUERY = '{0}/FILES/Excel/'.format(PATH)
    #         PATH_TXT = "{0}/FILES/TXT/Top_Rising.txt".format(PATH)
    #         while REPEAT < len(PalavraChave):  
    #             Valida_Connection()
    #             QueryString = str(PalavraChave[REPEAT]) 
    #             pytrend.build_payload(kw_list=[QueryString],timeframe=self, geo="BR")
    #             related_topcs_dict = pytrend.related_queries()
    #             PrettyArq =  str(related_topcs_dict.get(QueryString))
    #             with open(PATH_TXT, 'a', encoding='utf-8', newline="") as Criar:
    #                 Criar.write(PrettyArq.replace("{","").replace(":", "").replace("'top'","").replace("query","").replace("value","").replace("'","").replace("rising","").replace("}","").replace(",","").replace("None",""))
    #                 Criar.close()
    #             with open(PATH_TXT, 'r', encoding='utf-8', newline="") as abrir:
    #                 for limpar in abrir:
    #                     limpar = limpar.rstrip()
    #                     if limpar !="":
    #                         SAVE.append(limpar)
    #                 abrir.close()
    #                 os.remove(PATH_TXT)
    #             if not SAVE:
    #                 print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM CONSULTA RELACIONADA\n".format(QueryString))
    #                 REPEAT = REPEAT+1
    #             else:
    #                 for saves in SAVE:
    #                     if COUNT == int((saves[:2]).rstrip().lstrip()):
    #                         ListValue['Top'].append((saves[:2]).rstrip().lstrip())
    #                         ListValue['Values'].append((saves[int(len(saves)-6):]).rstrip().lstrip()) 
    #                         ListValue['Consultas Relacionadas'].append(saves[2:int(len(saves)-6)].strip().lstrip())  
    #                         ListValue['Termo Buscado'].append(QueryString)
    #                         ListValue['Tipo'].append('Em Ascensão')
    #                         ListValue['Data de Extração'].append(time.strftime("%d/%m/%Y %H:%M"))
    #                         ListValue['Periodo'].append(self)
    #                         COUNT = COUNT+1
    #                     else:
    #                         ListValue['Top'].append((saves[:2]).rstrip().lstrip())
    #                         ListValue['Values'].append((saves[int(len(saves)-6):]).rstrip().lstrip())    
    #                         ListValue['Consultas Relacionadas'].append(saves[2:int(len(saves)-6)].strip().lstrip())
    #                         ListValue['Termo Buscado'].append(QueryString)
    #                         ListValue['Tipo'].append('Principais')
    #                         ListValue['Data de Extração'].append(time.strftime("%d/%m/%Y %H:%M"))
    #                         ListValue['Periodo'].append(self)
    #                         COUNT = COUNT+1
    #                 COUNT = 0
    #                 SAVE.clear()
    #                 REPEAT = REPEAT+1

    #         Save_Csv.SaveRelated(ListValue, '{0}/Consultas_Relacionada.xlsx'.format(PATH_QUERY))                     
    #         print(".............TESTE << RELATED QUERIES >> FINALIZADO...............\n")
    #     except Exception as Erro:
    #         print("def NewRelatedQueries Erro:{0}".format(Erro))
#