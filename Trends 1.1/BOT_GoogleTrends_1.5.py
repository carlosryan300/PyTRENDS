import csv
import json
import os
import socket
import sys
import time
from os import path

import gspread
from oauth2client.service_account import ServiceAccountCredentials as OSS
from pytrends.request import TrendReq

#GLOBALS VARIÁVEIS
PATH = 'C:/ARQUIVOS-TRENDS/'
MODE = 'a','w','r'
ENCODING = "utf-8"
URLCONFIAVEIS= ['www.google.com', 'www.yahoo.com', "www.uol.com"]
VAR_GOOGLE =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDENCIAIS = OSS.from_json_keyfile_name('{0}/JSON/bot-carregamento-whp.json'.format(PATH), VAR_GOOGLE)
AUTORIZA = gspread.authorize(CREDENCIAIS)
DATA_HORA = time.strftime("%d/%m/%y %H:%M:%S")
SAVE = []
REPEAT = 0
COUNT = 0
#GLOBALS VARIÁVEIS

class GoogleTrends():
    def __init__():
        pass
    def KeyWords():
        KeyWords = []
        os.makedirs("{0}/TXT/".format(PATH),exist_ok=True)

        if path.isfile("{0}/TXT/KEYWORD.TXT".format(PATH))==True:
            pass
        else:
            print("..........DESCULPE NÃO CONSEGUI ACHAR O ARQUIVO KEYWORD.TXT............\n")
            print("..................VOU CRIAR PARA VOCÊ, SÓ UM SEGUNDO...................\n")
            time.sleep(3)
            with open("{0}/TXT/KEYWORD.TXT".format(PATH), 'a', encoding=ENCODING) as CRIAR:
                CRIAR.close()
            print("....PRONTO CRIEI, POR FAVOR ADICIONE AS PALAVRAS QUE DESEJA BUSCAR!....\n")
            Valida = False
            while Valida==False:
                S_N = str(input("DESEJA ADICIONAR AS PALAVRAS AGORA OU QUER FECHA O PROGRAMA? S/N:")).upper()
                if S_N == "S":
                    print("..QUANDO TERMINAR DE ESCREVER TODAS AS PALAVRAS, DIGITE @ E DÊ ENTER!..\n")
            
                    variavel = False
                    GuardaPalavras = []
                    while variavel==False:
                        Palavras = str(input("DIGITE A PALAVRA QUE DESEJA PESQUISAR:"))
                        if Palavras != "@" and len(Palavras)>1:
                            GuardaPalavras.append(Palavras)
                        elif Palavras=="@":
                            variavel = True                    
                        else:
                            print("AS PALAVRAS NÃO PODEM TER NÚMERO, CARACTERES ESPECÍAIS OU TER MENOS DE 3 LETRAS")
                    with open("{0}/TXT/KEYWORD.TXT".format(PATH), 'a', encoding=ENCODING, newline="") as CRIAR:
                        for palavra in GuardaPalavras:
                            palavra = palavra.rstrip()
                            if palavra != " " or palavra != "":
                                CRIAR.write("{0}\n".format(palavra))
                        CRIAR.close()
                        print(".....PRONTO PALAVRAS ADICIONADAS COM SUCESSO! O TESTE IRÁ CONTINUA.....\n")
                    Valida = True
                elif S_N == "N":
                    print("..........................FECHANDO PROGRAMA............................\n")
                    time.sleep(5)
                    sys.exit()
                else:
                    print("............................OPÇÃO INVÁLIDA.............................\n")         
    #VERIFICA SE O ARQUIVO ESTÁ VÁZIO      
        with open("{0}/TXT/KEYWORD.TXT".format(PATH),'r',encoding=ENCODING) as KEYWORDPARAMENT:
            for WordParament in KEYWORDPARAMENT:
                WordParament = WordParament.rstrip()
                if WordParament !="":
                    KeyWords.append(WordParament)
            if not KeyWords:
                print("..........OPS...NÃO HÁ NENHUMA PALAVRA NO ARQUIVO KEYWORD.TXT..........\n")
                time.sleep(5)
                print("........O PROGRAMA SERÁ FECHADO EM 7 SEG, ADICIONE AS PALAVRAS!........\n")
                time.sleep(7)
                sys.exit() 
            KEYWORDPARAMENT.close()
            return KeyWords
    #VERIFICA SE O ARQUIVO ESTÁ VÁZIO   
    def TOP_AND_RISING(Date):
        pytrend = TrendReq(hl='pt-BR',tz=-180, geo='BR')    
        PalavraChave = GoogleTrends.KeyWords()
        REPEAT = 0
        COUNT = 0
        PATH_RISING = '{0}CSV/RISING.csv'.format(PATH)
        PATH_TOP = '{0}CSV/TOP.csv'.format(PATH)
        PATH_TXT = "{0}TXT/Top_Rising.txt".format(PATH)
        while REPEAT < len(PalavraChave):  
        #PARTE 1
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("==================NÃO FOI POSSIVEL CONECTAR A INTERNET================\n")
            QueryString = str(PalavraChave[REPEAT]) 
            
            #CONTRUÇÃO DE QUERY DE PESQUISA
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

                        sheet =  AUTORIZA.open("TOP").sheet1
                        sheet.append_row([posicao, query.upper(), int(valor), DATA_HORA,QueryString.upper(), Date])
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
                        sheet =  AUTORIZA.open("RISING").sheet1
                        sheet.append_row([posicao, query.upper(), valor, DATA_HORA, QueryString.upper(), Date])
                        COUNT = COUNT+1
                SAVE.clear()
                REPEAT = REPEAT+1
                COUNT = 0
        print(".................TESTE << TOP AND RESING >> FINALIZADO.................\n")

    def OVER_TIME_INTEREST(Date):
        pytrend = TrendReq(hl='pt-BR',tz=240, geo='BR')
        PalavraChave = GoogleTrends.KeyWords()
        REPEAT = 0
        COUNT = 0
        PATH_OVER_CSV = "{0}CSV/INTERESSE_POR_DATA.csv".format(PATH) 
        PATH_OVER_TXT = "{0}TXT/Interesed.txt".format(PATH)

        while REPEAT < len(PalavraChave):  
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("==================NÃO FOI POSSIVEL CONECTAR A INTERNET================\n")
            QueryString = str(PalavraChave[REPEAT]) 
    
            #CONTRUÇÃO DE QUERY DE PESQUISA
            pytrend.build_payload(kw_list=[QueryString],timeframe=Date, geo="BR")
            
            #INTEREST OVER TIME
            interest_over_time_df = pytrend.interest_over_time()
            if interest_over_time_df.empty:
                print(".A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM INTERESSE POR DATA.".format(QueryString))
                REPEAT = REPEAT+1
            else:
                texto = str(interest_over_time_df[["{0}".format(QueryString)]]).replace("date","").replace(" ","").replace(QueryString, "")
                with open(PATH_OVER_TXT,'w', encoding=ENCODING, newline="") as primeira:
                    primeira.write(texto)
                    primeira.close()
                with open(PATH_OVER_TXT,'r', encoding=ENCODING, newline="") as segunda:
                    for limpa in segunda:
                        limpa = limpa.rstrip()
                        alter = limpa[:4]
                        if limpa !="" and alter.isnumeric()==True:
                            SAVE.append(limpa)
                    segunda.close()
                    os.remove(PATH_OVER_TXT)
                for saves in SAVE:
                    if path.isfile(PATH_OVER_CSV)==True:
                        with open(PATH_OVER_CSV, 'a',newline="", encoding=ENCODING) as Interesse:
                            try:
                                SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" )   
                                if Date=="now 1-H" or Date=="now 1-d" or Date=="now 7-d": 
                                    DataHora = "{0} {1}".format(saves[:10],saves[10:18])
                                    SalvaInteresse.writerow([DataHora, saves[18:], QueryString.upper(), DATA_HORA, Date])
                                else:
                                    SalvaInteresse.writerow([saves[:10], saves[10:], QueryString.upper(), DATA_HORA, Date])
                            finally:
                                Interesse.close()   
                    else:
                        with open(PATH_OVER_CSV, 'a',newline="", encoding=ENCODING) as Interesse: 
                            try:
                                SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" ) 
                                SalvaInteresse.writerow(["DATA", "VALOR", "QUERY", "DATA DE EXTRAÇÃO", "PERÍODO"])    
                                if Date=="now 1-H" or Date=="now 1-d" or Date=="now 7-d": 
                                    DataHora = ("{0} {1}".format(saves[:10],saves[10:18]))
                                    SalvaInteresse.writerow([DataHora, saves[18:], QueryString.upper(), DATA_HORA, Date])
                                else:
                                    SalvaInteresse.writerow([saves[:10], saves[10:], QueryString.upper(), DATA_HORA, Date])
                            finally:
                                Interesse.close()
                    time.sleep(1)
                    sheet =  AUTORIZA.open("INTERESSE_POR_TEMPO").sheet1
                    if Date=="now 1-H" or Date=="now 1-d" or Date=="now 7-d":
                        DataHora = ("{0} {1}".format(saves[:10],saves[10:18]))
                        sheet.append_row([DataHora, saves[18:], QueryString.upper(), DATA_HORA, Date])
                    else: 
                        sheet.append_row([saves[:10], int(saves[10:]), QueryString.upper(), DATA_HORA, Date])
                SAVE.clear()
                REPEAT = REPEAT+1
        print("...............TESTE << OVER TIME INTEREST >> FINALIZADO...............\n")

    def INTEREST_BY_REGION(Date):
        pytrend = TrendReq(hl='pt-BR', tz=-180, geo='BR')
        PalavraChave = GoogleTrends.KeyWords()
        REPEAT = 0
        COUNT = 0
        PATH_BY_REGION = "{0}CSV/INTERESSE_POR_REGION.csv".format(PATH)
        while REPEAT < len(PalavraChave):  
            if Validacoes.ChecaConexão()==True:
                pass
            else:
                print("==================NÃO FOI POSSIVEL CONECTAR A INTERNET================\n")
            QueryString = str(PalavraChave[REPEAT]) 
    
            #CONTRUÇÃO DE QUERY DE PESQUISA
            pytrend.build_payload(kw_list=[QueryString],timeframe=Date, geo="BR")

            interest_by_region_df = pytrend.interest_by_region()
            valores = interest_by_region_df.values
            i = 0
            param = 0
            while i < len(valores):
                param=param+valores[i]
                i = i+1    
            if int(param)==0:
                print("A PALAVRA: {0} NÃO TEM NENHUM DADO A SER COLETADO EM INTERESSE POR REGIÃO".format(QueryString))
                REPEAT = REPEAT+1
            else:
                if path.isfile(PATH_BY_REGION)==True:
                    interest_by_region_df.to_csv(PATH_BY_REGION, sep=";", mode='a')
                else:
                    with open(PATH_BY_REGION,'a', encoding=ENCODING, newline="") as CreatCSV:
                        csv.writer(CreatCSV)
                        CreatCSV.close()
                        interest_by_region_df.to_csv(PATH_BY_REGION, sep=";", mode='a',) 
                REPEAT = REPEAT+1

            with open(PATH_BY_REGION, 'r', encoding=ENCODING) as opencsv:
                arm = opencsv.readlines()
                opencsv.close()
                Estado = ""
                Valor = ""
                os.remove(PATH_BY_REGION)
                for arms in arm:
                    arms = arms.rstrip().replace("geoName;{0}".format(QueryString),"").replace("State of ", "").replace("Federal District", "Distrito Federal")
                    if arms !="":
                        Estado = str(arms[:len(arms)-3])
                        j = str(arms[len(arms)-2:]).replace(";","")
                        if j == "0" or int(j) < 10 and int(j)> 0:
                            Estado = str(arms[:len(arms)-2])
                        else:
                            pass
                        Valor = arms[len(Estado):].replace(";","")
                        if path.isfile("{0}CSV/INTERESSE_POR_REGIÃO.csv".format(PATH))==False:
                            with open("{0}CSV/INTERESSE_POR_REGIÃO.csv".format(PATH), 'a', newline="", encoding=ENCODING) as Interesse:
                                try:
                                    SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" ) 
                                    SalvaInteresse.writerow(["ESTADOS","VALOR","DATA E HORA","QUERY", "PERÍODO"])    
                                    SalvaInteresse.writerow([Estado.replace(";",""), int(Valor), QueryString.upper(), DATA_HORA, Date])
                                finally:
                                    Interesse.close()
                        else:
                            with open("{0}CSV/INTERESSE_POR_REGIÃO.csv".format(PATH), 'a', newline="", encoding=ENCODING) as Interesse:
                                try:
                                    SalvaInteresse = csv.writer(Interesse, delimiter=";", dialect="excel" )    
                                    SalvaInteresse.writerow([Estado.replace(";",""), int(Valor), QueryString.upper(), DATA_HORA, Date])
                                finally:
                                    Interesse.close()
                        time.sleep(1)
                        sheet =  AUTORIZA.open("INTERESSE_POR_REGIÃO").sheet1
                        sheet.append_row([Estado.replace(";",""), int(Valor), QueryString.upper(), DATA_HORA, Date])

        print(".................TESTE << OVER BY REGION >> FINALIZADO.................\n")
class Validacoes():  
    def __init__():
        pass
    
    def OpcoesDeRelatorios():

        check = False
        while check==False:
            if Validacoes.ChecaConexão()==True:
                check=True
                pass
            else:
            #prints
                print("..Opss! NÃO HÁ CONEXÃO COM A INTERNET, POR FAVOR VERIFIQUE A CONEXÃO!..")
                print("===============EM UM MINUTO TENTAREI EXECUTAR NOVAMENTE!===============")
            #prints
                time.sleep(60)
    #prints
        print("\n")
        print(" 1 - TOP AND RISING!      | TRARÁ OS DADOS REFERÊNTE A TOP E TENDÊNCIA")                
        print(" 2 - OVER TIME INTERESSE! | TRARÁ OS DADOS REFERÊNTE AS KEYWORDS POR INTERESSE E TEMPO")                  
        print(" 3 - INTEREST BY REGION!  | TRARÁ OS DADOS REFERÊNTE AS KEYWORDS POR REGIÃO")
        print(" 4 - ALL!                 | TRARÁ OS DADOS DE TODAS OPÇÕES ACIMA")
        print(" 5 - CANCELAR!            | FECHARÁ O APLICATIVO") 
        print("\n")  
        validador = False
        while validador == False:
            alternativa = str(input("DIGITE O NÚMERO DA ALTERNATIVA:"))
            print("\n")
            os.makedirs("{0}/CSV/".format(PATH),exist_ok=True)
            if alternativa.isnumeric()==True and int(alternativa)==1:
                Date =  Validacoes.OpcaoDeData()               
                GoogleTrends.TOP_AND_RISING(Date)
                validador = True
            elif alternativa.isnumeric()==True and int(alternativa)==2:
                Date =  Validacoes.OpcaoDeData()
                GoogleTrends.OVER_TIME_INTEREST(Date)
                validador = True
            elif alternativa.isnumeric()==True and int(alternativa)==3:
                Date =  Validacoes.OpcaoDeData()
                GoogleTrends.INTEREST_BY_REGION(Date)
                validador = True
            elif alternativa.isnumeric()==True and int(alternativa)==4:
                Date =  Validacoes.OpcaoDeData()
                GoogleTrends.TOP_AND_RISING(Date)
                GoogleTrends.OVER_TIME_INTEREST(Date)
                GoogleTrends.INTEREST_BY_REGION(Date)
                validador = True   
                
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
                print("|===================================ALTERNATIVA INVÁLIDA================================|\n")

    def OpcaoDeData(): 
    #prints
        print("     BASE  |   TEMPO   | TITULO")
        print(" 1 - AGORA |   1-H     | BUSCA DADOS DA ÚLTIMA HORA, SENDO AGORA O HORÁRIO BASE!")
        print(" 2 - AGORA |   1-D     | BUSCA DADOS DE 1 DIA, SENDO HOJE O DIA DE BASE!")
        print(" 3 - AGORA |   7-D     | BUSCA DADOS DOS ÚLTIMAS 7 DÍAS, SENDO HOJE O DIA DE BASE!") 
        print(" 4 - HOJE  |   1-MÊS   | BUSCA DADOS DE 1 MÊS ATRÁS, SENDO HOJE O DIA DE BASE!")
        print(" 5 - HOJE  |   3-MÊSES | BUSCA DADOS DOS ÚLTIMOS 3 MÊS, SENDO HOJE O DIA DE BASE!")
        print(" 6 - HOJE  |   5-ANOS  | BUSCA DADOS DOS ÚLTIMOS 5 ANOS, SENDO HOJE O DIA DE BASE!")
        print(" 7 - INICIO|   FIM     | BUSCA DADOS COM A DATA PESSONALIZADA (NO FORMATO A-M-D)")
        print(" 8 - HOJE  |   TODOS   | BUSCA DADOS DE TODOS OS PÉRIODOS ATÉ HOJE")
        print("\n")
        valida = False
        while valida == False: 

            alternativa = str(input("DIGITE O NÚMERO DA ALTERNATIVA:"))

            print("\n")
            
            if alternativa.isnumeric()==True and int(alternativa)==1:
                return "now 1-H"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==2:
                return "now 1-d"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==3:
                return "now 7-d"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==4:
                return "today 1-m"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==5:   
                return "today 3-m"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==6:
                return "today 5-y"
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==7:
                Ini = str(input("DATA INICIAL EXEMPLO(2017-01-30):"))
                Fim = str(input("DATA FINAL EXEMPLO(2017-12-31):"))   
                print("\n")             
                return "{0} {1}".format(Ini, Fim)
                valida = True
            elif alternativa.isnumeric()==True and int(alternativa)==8:
                return "all"
                valida = True
            else:
                print("===========================ALTERNATIVA INVÁLIDA========================\n")
                valida = False

    def ChecaConexão():
        global URLConfiaveis
        for URLS in URLCONFIAVEIS:
            a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            a.settimeout(.5)
            try:
                b = a.connect_ex((URLS, 80))
                if b==0: #ok, conectado
                    return True
            except:
                pass
            a.close()
        return False


Validacoes.OpcoesDeRelatorios()
