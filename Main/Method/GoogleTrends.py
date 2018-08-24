import csv, os, os.path as path, sys, time, pandas as pd
from openpyxl.workbook import Workbook
from pytrends.request import TrendReq
from Validation.Method.Connection_Network import Valida_Connection
from Validation.Method.List_KeyWord import *
from Saves.Save_Csv import *
from Saves.Save_BigQuery import *
from Saves.Save_GSheets import *

PATH = os.getcwd()

class GoogleTrends():
    def __init__():
        pass
    def NewByRegion(self, ModeSave):
        global PATH
        Local = "{0}/FILES/Excel/ByRegion.csv".format(PATH)
        i = 1
        RegAndImp()
        try:
            Repeat = NumberKey()
            while i <= Repeat:
                KeyWords = List_KeyWords()
                if KeyWords != "" or KeyWords!=None:
                    pytrend = TrendReq(hl='pt-BR', geo='BR')
                    Valida_Connection()
                    pytrend.build_payload(kw_list=KeyWords,timeframe=self, geo="BR")
                    interest_by_region_df = pytrend.interest_by_region()
                    interest_by_region_df.to_csv(Local)
                    df_dataFrame = pd.DataFrame(pd.read_csv(Local))
                    os.remove(Local)
                    if ModeSave==1:
                        Save_Csv.PrepareValue(df_dataFrame,'geoName', 'By_Region', KeyWords, self)
                    elif ModeSave==2:
                        PrepareList('By_Region', df_dataFrame, "geoName",KeyWords, self)
                    elif ModeSave==3:
                        Save_Csv.PrepareValue(df_dataFrame,'geoName', 'By_Region', KeyWords, self)
                        PrepareList('By_Region', df_dataFrame, "geoName",KeyWords, self)
                i = i + 1
            print(".................TESTE << POR REGIÃO >> FINALIZADO.................\n")
        except Exception as Erro:
            print("def New_By_Region -> Ocorreu o Erro:{0}".format(Erro))
        ZerarI()
    def NewOverTime(self, ModeSave):
        global PATH
        Local = "{0}/FILES/Excel/OverTime.csv".format(PATH)
        i = 1
        RegAndImp()
        try:
            Repeat = NumberKey()
            while i <= Repeat:
                KeyWords = List_KeyWords()
                if KeyWords != "" or KeyWords!=None:
                    pytrend = TrendReq(hl='pt-BR', geo='BR')
                    Valida_Connection()
                    pytrend.build_payload(kw_list=KeyWords,timeframe=self, geo="BR")
                    interest_over_time_df = pytrend.interest_over_time()
                    interest_over_time_df.to_csv(Local, decimal=',')
                    df_dataFrame = pd.DataFrame(pd.read_csv(Local))
                    os.remove(Local)
                    if ModeSave==1:
                        Save_Csv.PrepareValue(df_dataFrame, 'date', 'Over_Time', KeyWords, self)
                    elif ModeSave==2:
                        PrepareList('Over_Time', df_dataFrame, 'date', KeyWords, self)
                    elif ModeSave==3:
                        Save_Csv.PrepareValue(df_dataFrame, 'date', 'Over_Time', KeyWords, self)
                        PrepareList('Over_Time', df_dataFrame, 'date', KeyWords, self)
                i = i + 1
            print(".................TESTE << POR TEMPO >> FINALIZADO.................\n")
        except Exception as Erro:
            print("def New_Over_Time -> Ocorreu o Erro:{0}".format(Erro))  
        ZerarI()
    def NewRelatedQueries(self, ModeSave):
        PATH_QUERY = '{0}/FILES/Excel/RelatedQueries.csv'.format(PATH)
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
                if ModeSave==1:
                    Save_Csv.SaveRelated(ListValue,'{0}'.format(PATH_QUERY))
                elif ModeSave==2:
                    PrepareListOverTime('Related_Queries', ListValue)
                elif ModeSave==3:
                    Save_Csv.SaveRelated(ListValue,'{0}'.format(PATH_QUERY))
                    PrepareListOverTime('Related_Queries', ListValue)
            print("............TESTE << CONSULTAS RELACIONADAS >> FINALIZADO...........\n")   
        except Exception as Erro:
            print("def NewRelatedQueries ->Ocorreo o Erro:{0}".format(Erro))
    def NewRelatedTopics(self, ModeSave): 
        PATH_QUERY = '{0}/FILES/Excel/RelatedTopics.csv'.format(PATH)
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
                    'Assuntos Relacionadas':[], #Não adicionar
                    'Values':[], #Não adicionar
                    'Tipo':[], #Não adicionar
                    'Termo Buscado':[],
                    'Data de Extração':[],
                    'Periodo':[]
                }
                LenInTop = len(list(related_topcs_dict[QueryString]['title']))
                for i in (range(0, LenInTop)):
                    ListValue['Top'].append(i)
                    ListValue['Termo Buscado'].append(QueryString)
                    ListValue['Data de Extração'].append(Time)
                    ListValue['Periodo'].append(self)                    
                ListValue.update({'Assuntos Relacionadas': list(related_topcs_dict[QueryString]['title'])})
                ListValue.update({'Values': list(related_topcs_dict[QueryString]['value'])})
                ListValue.update({'Tipo': list(related_topcs_dict[QueryString]['type'])})
                if ModeSave==1:
                    Save_Csv.SaveRelated(ListValue,'{0}'.format(PATH_QUERY))
                elif ModeSave==2:
                    PrepareListOverTime('Related_Topics', ListValue)
                elif ModeSave==3:
                    Save_Csv.SaveRelated(ListValue,'{0}'.format(PATH_QUERY))
                    PrepareListOverTime('Related_Topics', ListValue)
            print("...........TESTE << ASSUNTOS RELACIONADOS >> FINALIZADO...........\n")   
        except Exception as Erro:
            print("def NewRelatedQueries ->Ocorreo o Erro:{0}".format(Erro))