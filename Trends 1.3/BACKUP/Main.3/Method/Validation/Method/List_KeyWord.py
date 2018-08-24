import os, time, sys, os.path as path
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
    KeyWords = []
    os.makedirs("{0}/FILES/TXT/".format(PATH),exist_ok=True)

    if path.isfile("{0}/FILES/TXT/KEYWORD.TXT".format(PATH))==True:
        pass
    else:
        print("..........DESCULPE NÃO CONSEGUI ACHAR O ARQUIVO KEYWORD.TXT............\n")
        print("..................VOU CRIAR PARA VOCÊ, SÓ UM SEGUNDO...................\n")
        time.sleep(3)
        with open("{0}/FILES/TXT/KEYWORD.TXT".format(PATH), 'a', encoding="utf-8") as CRIAR:
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
                with open("{0}/FILES/TXT/KEYWORD.TXT".format(PATH), 'a', encoding="utf-8", newline="") as CRIAR:
                    for palavra in GuardaPalavras:
                        palavra = palavra.rstrip()
                        if palavra != " " or palavra != "":
                            CRIAR.write("{0}\n".format("{}\n".format(palavra)))
                    CRIAR.close()
                    print(".....PRONTO PALAVRAS ADICIONADAS COM SUCESSO! O TESTE IRÁ CONTINUA.....\n")
                Valida = True
            elif S_N == "N":
                print("..........................FECHANDO PROGRAMA............................\n")
                time.sleep(5)
                sys.exit()
            else:
                print("............................OPÇÃO INVÁLIDA.............................\n")
    with open("{0}/FILES/TXT/KEYWORD.TXT".format(PATH),'r',encoding="utf-8") as KEYWORDPARAMENT:
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
def RegAndImp():
    global Implementador
    global Regulador
    Implementador = 1
    Regulador = 1
