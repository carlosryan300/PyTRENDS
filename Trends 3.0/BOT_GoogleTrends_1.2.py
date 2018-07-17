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
        path = RemoveAndAdd.getcwd()
        RemoveAndAdd.makedirs("{0}/TXT/".format(path),exist_ok=True)
        if isFile.isfile("TXT/KEYWORD.TXT")==True:
            pass
        else:
            print("DESCULPE NÃO CONSEGUI ACHAR O ARQUIVO KEYWORD.TXT\n")
            data.sleep(5)
            print("VOU CRIAR PARA VOCÊ, SÓ UM SEGUNDO\n")
            data.sleep(5)
            with open("TXT/KEYWORD.TXT", "w") as CRIAR:
                CRIAR.close()
            print("PRONTO CRIEI, ESTÁ DENTRO DA PASTA TXT/KEYWORD.TXT, POR FAVOR ADICIONE AS PALAVRAS QUE DESEJA BUSCAR!\n")
            data.sleep(5)
            print("O PROGRAMA SERÁ FECHADO EM 10 SEG, APÓS ADIONAR AS PALAVRAS EXECUTE O PROGRAMA NOVAMENTE!\n")
            data.sleep(10)
            sys.exit()
        
        with open("TXT/KEYWORD.TXT","r", encoding="utf-8") as KEYWORDPARAMENT:
            for WordParament in KEYWORDPARAMENT:
                WordParament = WordParament.rstrip()
                if WordParament !="":
                    KeyWords.append(WordParament)
            if not KeyWords:
                print("OPS...NÃO HÁ NENHUMA PALAVRA NO ARQUIVO KEYWORD.TXT\n")
                data.sleep(5)
                print("O PROGRAMA SERÁ FECHADO EM 10 SEG, APÓS ADIONAR AS PALAVRAS EXECUTE O PROGRAMA NOVAMENTE!\n")
                data.sleep(10)
                sys.exit() 
            KEYWORDPARAMENT.close()
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
            with open("TXT/Top_Rising.txt","a", encoding="utf-8") as Criar:
                Criar.write(PrettyArq.replace("{","").replace(":", "").replace("'top'","").replace("query","").replace("value","").replace("'","").replace("rising","").replace("}","").replace(",","").replace("None",""))
                Criar.close()

            with open("TXT/Top_Rising.txt", "r", encoding="utf-8") as abrir:
                for limpar in abrir:
                    limpar = limpar.rstrip()
                    if limpar !="":
                        save.append(limpar)
                abrir.close()
                RemoveAndAdd.remove("TXT/Top_Rising.txt")
            if not save:
                print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM TOP E TENDÊNCIA".format(QueryString))
                repeat = repeat+1
            else:
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
        print("TESTE << TOP AND RESING REGION >> FINALIZADO")

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
            if interest_over_time_df.empty:
                print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM INTERESSE POR DATA".format(QueryString))
                repeat = repeat+1
            else:
                texto = str(interest_over_time_df[["{0}".format(QueryString)]]).replace("date","").replace(" ","").replace(QueryString, "")
                with open("TXT/Interesed.txt",'w') as primeira:
                    primeira.write(texto)
                    primeira.close()
                with open("TXT/Interesed.txt",'r') as segunda:
                    for limpa in segunda:
                        limpa = limpa.rstrip()
                        if limpa !="":
                            save.append(limpa)
                    segunda.close()
                    RemoveAndAdd.remove("TXT/Interesed.txt")
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
        print("TESTE << OVER TIME INTEREST >> FINALIZADO")

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
            valores = interest_by_region_df.values
            i = 0
            valor = 0
            while i < len(valores):
                valor=valor+valores[i]
                i = i+1    
            if int(valor)==0:
                print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM INTERESSE POR REGIÃO".format(QueryString))
                repeat = repeat+1
            else:
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
                
            elif alternativa.isnumeric()==True and int(alternativa)==2:
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_DATA".format(path),exist_ok=True)
                GoogleTrends.OVER_TIME_INTEREST()
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==3:
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_REGIÃO".format(path),exist_ok=True) 
                GoogleTrends.INTEREST_BY_REGION()
                valida = True
                print("TESTES << INTEREST BY REGION >> FINALIZADO")
            elif alternativa.isnumeric()==True and int(alternativa)==4:
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TOP".format(path),exist_ok=True)
                RemoveAndAdd.makedirs("{0}/CSV/TOP_E_TENDENCIA/TENDENCIA".format(path),exist_ok=True) 
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_REGIÃO".format(path),exist_ok=True) 
                RemoveAndAdd.makedirs("{0}/CSV/INTERESSE_POR_DATA".format(path),exist_ok=True)
                GoogleTrends.TOP_AND_RISING()
                GoogleTrends.OVER_TIME_INTEREST()
                GoogleTrends.INTEREST_BY_REGION()
                valida = True   
                
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
