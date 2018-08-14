from Validation.Method.Connection_Network import Valida_Connection
import os 
from GoogleTrends import GoogleTrends

PATH = os.getcwd()

def Report_Option():    
    Valida_Connection()
    print("\n")
    print(" 1 - CONSULTAS RELACIONADAS | TRARÁ OS DADOS REFERÊNTE A TOP E TENDÊNCIA")                
    print(" 2 - INTERESSE POR TEMPO    | TRARÁ OS DADOS REFERÊNTE AS KEYWORDS POR INTERESSE E TEMPO")                  
    print(" 3 - INTERESSE POR REGIÕES  | TRARÁ OS DADOS REFERÊNTE AS KEYWORDS POR REGIÃO")
    print(" 4 - ALL!                   | TRARÁ OS DADOS DE TODAS OPÇÕES ACIMA")
    print(" 5 - CANCELAR!              | FECHARÁ O PROGRAMA") 
    print("\n")  
    validador = False
    while validador == False:
        alternativa = str(input("DIGITE O NÚMERO DA ALTERNATIVA:"))
        print("\n")
        os.makedirs("{0}/FILES/Excel/".format(PATH),exist_ok=True)
        if alternativa.isnumeric()==True and int(alternativa)==1:
            Date =  OptionDate() 
            GoogleTrends.NewRelatedQueries(Date)              
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==2:
            Date =  OptionDate()
            GoogleTrends.NewOverTime(Date)
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==3:
            Date =  OptionDate()
            GoogleTrends.NewByRegion(Date)
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==4:
            Date =  OptionDate()
            GoogleTrends.NewOverTime(Date)
            GoogleTrends.NewByRegion(Date)
            GoogleTrends.NewRelatedQueries(Date) 
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

def OptionDate(): 

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

Report_Option()        