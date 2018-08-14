import csv
import json
import os as RemoveAndAdd
import os.path as isFile
import socket
import sys
import time as data

from pytrends.request import TrendReq

URLConfiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']

class GoogleTrends():
    def __init__():
        pass
    def KeyWords():
        KeyWords = []
        with open("TXT/KEYWORD.TXT","r", encoding="utf-8") as KEYWORDPARAMENT:
            for WordParament in KEYWORDPARAMENT:
                WordParament = WordParament.rstrip()
                if WordParament !="":
                    KeyWords.append(WordParament)
            return KeyWords

    def TOP_AND_RISING():
        pytrend = TrendReq()
        repeat = 0
        count = 0
        PalavraChave = GoogleTrends.KeyWords()
        save=[]
        while repeat < len(PalavraChave):  
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("===========NÃO FOI POSSIVEL CONECTAR A INTERNET===========")
            QueryString = str(PalavraChave[repeat]) 
            
            #CONTRUÇÃO DE QUERY DE PESQUISA
            pytrend.build_payload(kw_list=[QueryString],timeframe="today 1-m", geo="BR")
            
            #TOP AND RISING
            related_queries_dict = pytrend.related_queries()

            PrettyArq =  str(related_queries_dict.get(QueryString))
            with open("TXT/Arq.txt","a", encoding="utf-8") as Criar:
                Criar.write(PrettyArq.replace("{","").replace(":", "").replace("'top'","").replace("query","").replace("value","").replace("'","").replace("rising","").replace("}","").replace(",","").replace("None",""))
                Criar.close()

            with open("TXT/Arq.txt", "r", encoding="utf-8") as abrir:
                for limpar in abrir:
                    limpar = limpar.rstrip()
                    if limpar !="":
                        save.append(limpar)
                abrir.close()
                RemoveAndAdd.remove("TXT/Arq.txt")

            for saves in save:
                posicao = (saves[:2]).rstrip().lstrip()
                valor = (saves[int(len(saves)-6):]).rstrip().lstrip()     
                query = (saves[2:int(len(saves)-6)].strip().lstrip())
                if count == int(posicao):
                    if isFile.isfile('CSV/TOP_E_TENDENCIA/TOP/{0}_TOP.csv'.format(QueryString.upper()))==False:
                        with open('CSV/TOP_E_TENDENCIA/TOP/{0}_TOP.csv'.format(QueryString.upper()), 'a+', newline="", encoding="utf-8") as f:
                            wt = csv.writer(f, delimiter=";")   
                            wt.writerow(["Top","Palavra","Valores","Data de Extração"]) 
                            wt.writerow([posicao, query, valor, data.strftime("%d/%m/%y")])
                            f.close()
                    elif isFile.isfile('CSV/TOP_E_TENDENCIA/TOP/{0}_TOP.csv'.format(QueryString.upper()))==True:
                        with open('CSV/TOP_E_TENDENCIA/TOP/{0}_TOP.csv'.format(QueryString.upper()), 'a+', newline="", encoding="utf-8") as f:
                            wt = csv.writer(f, delimiter=";")     
                            wt.writerow([posicao, query, valor, data.strftime("%d/%m/%y")])
                            f.close() 
                    count = count+1
                else:
                    if isFile.isfile('CSV/TOP_E_TENDENCIA/TENDENCIA/{0}_RISING.csv'.format(QueryString.upper()))==False:
                        with open('CSV/TOP_E_TENDENCIA/TENDENCIA/{0}_RISING.csv'.format(QueryString.upper()), 'a+', newline="", encoding="utf-8") as f:
                            wt = csv.writer(f, delimiter=";")   
                            wt.writerow(["Top","Palavra","Valores", "Data de Extração"]) 
                            wt.writerow([posicao, query, valor, data.strftime("%d/%m/%y")])
                            f.close()
                    elif isFile.isfile('CSV/TOP_E_TENDENCIA/TENDENCIA/{0}_RISING.csv'.format(QueryString.upper()))==True:
                        with open('CSV/TOP_E_TENDENCIA/TENDENCIA/{0}_RISING.csv'.format(QueryString.upper()), 'a+', newline="", encoding="utf-8") as f:
                            wt = csv.writer(f, delimiter=";")     
                            wt.writerow([posicao, query, valor, data.strftime("%d/%m/%y")])
                            f.close()
                    count = count+1
            save.clear()
            repeat = repeat+1
            count = 0

    def OVER_TIME_INTEREST():
        pytrend = TrendReq()
        repeat = 0
        count = 0
        PalavraChave = GoogleTrends.KeyWords()
        save=[]
        while repeat < len(PalavraChave):  
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("===========NÃO FOI POSSIVEL CONECTAR A INTERNET===========")
            QueryString = str(PalavraChave[repeat]) 
    
            #CONTRUÇÃO DE QUERY DE PESQUISA
            pytrend.build_payload(kw_list=[QueryString],timeframe="today 1-m", geo="BR")
            
            #INTEREST OVER TIME
            interest_over_time_df = pytrend.interest_over_time()

            texto = str(interest_over_time_df[["{0}".format(QueryString)]]).replace("date","").replace(" ","").replace(QueryString, "")
            with open("TXT/texto.txt",'w') as primeira:
                primeira.write(texto)
                primeira.close()
            with open("TXT/texto.txt",'r') as segunda:
                for limpa in segunda:
                    limpa = limpa.rstrip()
                    if limpa !="":
                        save.append(limpa)
                segunda.close()
                RemoveAndAdd.remove("TXT/texto.txt") 
            for saves in save:
                if isFile.isfile("CSV/INTERESSE_POR_DATA/{0}_INTERESSE_POR_DATA.csv".format(QueryString.upper()))==True:
                        with open("CSV/INTERESSE_POR_DATA/{0}_INTERESSE_POR_DATA.csv".format(QueryString.upper()), 'a',newline="", encoding="utf-8") as Interesse:
                            try:
                                SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" )     
                                SalvaInteresse.writerow([saves[:10], saves[10:], QueryString])
                            finally:
                                Interesse.close()   
                elif isFile.isfile("CSV/INTERESSE_POR_DATA/{0}_INTERESSE_POR_DATA.csv".format(QueryString.upper()))==False: 
                        with open("CSV/INTERESSE_POR_DATA/{0}_INTERESSE_POR_DATA.csv".format(QueryString.upper()), 'a',newline="", encoding="utf-8") as Interesse: 
                            try:
                                SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" ) 
                                SalvaInteresse.writerow(["Data", "Valor", "Query"])    
                                SalvaInteresse.writerow([saves[:10], saves[10:], QueryString])
                            finally:
                                Interesse.close()
            save.clear()
            repeat = repeat+1

    def INTEREST_BY_REGION():
        pytrend = TrendReq()
        repeat = 0
        count = 0
        PalavraChave = GoogleTrends.KeyWords()
        save=[]
        while repeat < len(PalavraChave):  
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("===========NÃO FOI POSSIVEL CONECTAR A INTERNET===========")
            QueryString = str(PalavraChave[repeat]) 
    
            #CONTRUÇÃO DE QUERY DE PESQUISA
            pytrend.build_payload(kw_list=[QueryString],timeframe="today 1-m", geo="BR")

            interest_by_region_df = pytrend.interest_by_region()
            caminho = ("CSV/INTERESSE_POR_REGIÃO/{0}_INTERESSE_POR_REGIÃO_{1}.csv".format(QueryString.upper(),data.strftime("%d.%m.%y")))
            if isFile.isfile(caminho)==True:
                interest_by_region_df.to_csv(path_or_buf=caminho,sep=";", mode="a")
            elif isFile.isfile(caminho)==False:
                with open(caminho,"a", encoding="utf-8", newline="") as CreatCSV:
                    csv.writer(CreatCSV)
                    CreatCSV.close()
                    interest_by_region_df.to_csv(path_or_buf=caminho,sep=";", mode="a") 
            repeat = repeat+1

class Validacoes():  
    def __init__():
        pass
    
    def OpcoesDeRelatorios():
        valida = False
        while valida == False:
            check = False
            while check==False:
                if Validacoes.ChecaConexão()==True:
                    check=True
                    pass
                else:
                    print("...............OPS! NÃO HÁ CONEXÃO COM A INTERNET, POR FAVOR VERIFIQUE A CONEXÃO!..............")
                    print("======================== EM UM MINUTO TENTAREI EXECUTAR NOVAMENTE =============================")
                    time.sleep(60)
            print("QUAL OPÇÃO VOCÊ DESEJA EXECUTA?")
            print("1 - TOP AND RISING!")
            print("2 - OVER TIME INTERESSE!")
            print("3 - INTEREST BY REGION!")
            print("4 - ALL!")
            print("5 - CANCELAR!\n")

            alternativa = str(input("DIGITE O NÚMERO DA ALTERNATIVA:"))
            print("\n")
            path = RemoveAndAdd.getcwd()
            if alternativa.isnumeric()==True and int(alternativa)==1:
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TOP".format(path),exist_ok=True)
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TENDENCIA".format(path),exist_ok=True)                
                GoogleTrends.TOP_AND_RISING()
                valida = True
                print("TESTE |TOP AND RESING REGION| CONCLUIDO COM SUCESSO")
            elif alternativa.isnumeric()==True and int(alternativa)==2:
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_REGIÃO".format(path),exist_ok=True)
                GoogleTrends.OVER_TIME_INTEREST()
                valida = True
                print("TESTE |OVER TIME INTEREST| CONCLUIDO COM SUCESSO")
            elif alternativa.isnumeric()==True and int(alternativa)==3:
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_DATA".format(path),exist_ok=True)
                GoogleTrends.INTEREST_BY_REGION()
                valida = True
                print("TESTE |INTEREST BY REGION| CONCLUIDO COM SUCESSO")
            elif alternativa.isnumeric()==True and int(alternativa)==4:
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TOP".format(path),exist_ok=True)
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TENDENCIA".format(path),exist_ok=True) 
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_REGIÃO".format(path),exist_ok=True) 
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_DATA".format(path),exist_ok=True)
                GoogleTrends.TOP_AND_RISING()
                GoogleTrends.OVER_TIME_INTEREST()
                GoogleTrends.INTEREST_BY_REGION()
                valida = True   
                print("TESTES |TOP AND RESING, OVER TIME INTEREST E INTEREST BY REGION| CONCLUIDO COM SUCESSO")
            elif alternativa.isnumeric()==True and int(alternativa)==5:
                v = 0
                x = 6
                while v < 5:
                    v=v+1
                    x=x-1
                    time.sleep(1)
                    print("O PROGRAMA SERÁ FECHADO EM {0} SEGUNDOS".format(x))
                sys.exit()
            else:
                valida = False
                print("ALTERNATIVA INVÁLIDA")
            
    def ChecaConexão():
        global URLConfiaveis
        for urlconfiaveis in URLConfiaveis:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b = a.connect_ex((urlconfiaveis, 80))
                if b==0: #ok, conectado
                    return True

            except:
                pass
            a.close()
        return False
Validacoes.OpcoesDeRelatorios()
