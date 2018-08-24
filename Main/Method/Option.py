from Validation.Method.Connection_Network import Valida_Connection
import os, time,sys 
from GoogleTrends import GoogleTrends
PATH = os.getcwd()
def Report_Option():    
    Valida_Connection()
    print("===================SELECIONE UMA DAS OPÇÕES ABAIXO=================\n")
    print(" 1 - CONSULTAS RELACIONADAS | DADOS REFERÊNTE A KEYWORD POR CONSULTAS RELACIONADAS")    
    print(" 2 - ASSUNTOS RELACIONADOS  | DADOS REFERÊNTE A KEYWORD POR ASSUNTOS RELACIONADOS")               
    print(" 3 - INTERESSE POR TEMPO    | DADOS REFERÊNTE AS KEYWORDS POR INTERESSE E TEMPO")                  
    print(" 4 - INTERESSE POR REGIÕES  | DADOS REFERÊNTE AS KEYWORDS POR REGIÃO")
    print(" 5 - ALL!                   | DADOS DE TODAS OPÇÕES ACIMA")
    print(" 6 - CANCELAR!              | FECHARÁ O PROGRAMA") 
    print("\n")  
    validador = False
    while validador == False:
        alternativa = str(input(" DIGITE O NÚMERO DA ALTERNATIVA:"))
        print("\n")
        os.makedirs("{0}/FILES/Excel/".format(PATH),exist_ok=True)
        if alternativa.isnumeric()==True and int(alternativa)==1:
            Date =  OptionDate()
            ModeSave = ModoSave() 
            GoogleTrends.NewRelatedQueries(Date, ModeSave)              
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==2:
            Date =  OptionDate()
            ModeSave = ModoSave()
            GoogleTrends.NewRelatedTopics(Date, ModeSave)
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==3:
            Date =  OptionDate()
            ModeSave = ModoSave()
            GoogleTrends.NewOverTime(Date, ModeSave)
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==4:
            Date =  OptionDate()
            ModeSave = ModoSave()
            GoogleTrends.NewByRegion(Date, ModeSave)
            validador = True
        elif alternativa.isnumeric()==True and int(alternativa)==5:
            Date =  OptionDate()
            ModeSave = ModoSave()
            GoogleTrends.NewOverTime(Date, ModeSave)
            GoogleTrends.NewByRegion(Date, ModeSave)
            GoogleTrends.NewRelatedTopics(Date, ModeSave)
            GoogleTrends.NewRelatedQueries(Date, ModeSave)
            validador = True    
        elif alternativa.isnumeric()==True and int(alternativa)==6:
            v = 0
            x = 6
            while v < 5:
                v=v+1
                x=x-1
                time.sleep(1)
                print("O PROGRAMA SERÁ FECHADO EM {0} SEGUNDOS".format(x))
            sys.exit()
        else:
            print("OPÇÃO INVÁLIDA, DIGITE APENAS O NÚMERO DA ALTERNATIVA!\n")
def OptionDate(): 
    print("===================SELECIONE UMA DAS OPÇÕES ABAIXO=================\n")
    print("     PERIODO |   TEMPO")
    print(" 1 - HORA    |   1 HORA ATRÁS!")
    print(" 2 - HORA    |   7 HORAS ATRÁS!")
    print(" 3 - DIAS    |   7 DIAS ATRÁS!") 
    print(" 4 - MÊS     |   1 MÊS ATRÁS!")
    print(" 5 - MÊS     |   3 MÊSES ATRÁS!")
    print(" 6 - ANOS    |   5 ANOS ATRÁS!")
    print(" 7 - INICIO  |   FIM DATA PESSONALIZADA!")
    print(" 8 - ANOS    |   TODOS OS PERÍODOS!")
    print("\n")
    valida = False
    while valida == False: 
        alternativa = str(input(" DIGITE O NÚMERO DA ALTERNATIVA:"))
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
            print("OPÇÃO INVÁLIDA, DIGITE APENAS O NÚMERO DA ALTERNATIVA!\n")
            valida = False
def ModoSave():
    print("===================SELECIONE UMA DAS OPÇÕES ABAIXO=================\n")
    print(" 1 - SALVAR EM CSV")
    print(" 2 - SALVAR EM GOOGLE SHEETS")
    print(" 3 - SALVAR EM AMBOS\n")
    
    while True:
        opcao = str(input(" DIGITA O NÚMERO DA ALTERNATIVA:"))
        if opcao.isnumeric()==True and opcao=='1':
            return int(opcao)
        elif opcao.isnumeric()==True and opcao=='2':
            return int(opcao)
        elif opcao.isnumeric()==True and opcao=='3':
            return int(opcao)
        else:
            print("OPÇÃO INVÁLIDA, DIGITE APENAS O NÚMERO DA ALTERNATIVA!\n")

Report_Option()    
