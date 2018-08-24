import smtplib

def SendEmail(Assunto, Mensagem):
    email = ''
    password = ''
    msg = '\r\n'.join([
        'From: %s' % email,
        'To: %s' % email,
        'Subject: %s' % Assunto,
        '',
        '%s' % Mensagem
    ])
    # Enviando o email
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email,password)
    server.sendmail(email, email, msg)
    server.quit()










# Lista = 18
    # Fastest = int(Lista-1)%2
    # if Fastest==0:
    #     Retorno = (int(Lista-1)//4)
    # else:
    #     Retorno = (int(Lista-1)//4)+1

    #JEFF
    # import pandas as pd
    # path = "Caminho do Arquivo"
    # Read = pd.read_csv(path, sep=',', encoding='utf=8')
    # i = 0 #VARIÁVEL DE INCREMENTAÇÃO
    # ArqOne = [] #LISTA QUE RECEBERÁ TODOS DADOS ATÉ A METADE DO TAMANHO DE READ
    # ArqTwo = [] #LISTA QUE RECEBERÁ TODOS DADOS A PARTIT DA METADE DO TAMANHO DE READ
    # #ArqThree = [] Caso queirá separar por 3
    # for index, Reads in Read.iterrows():
    #     if (len(Read)/2)<=i:#CASO QUEIRÁ SEPARAR EM 3 A LISTA MUDE O NÚMERO DA DIVISÃO POR 3
    #         ArqOne.append(Reads)# ESSA LISTA RECEBERÁ A METADE OU 1 TERÇO DO TAMANHO DO CSV
    #         i=i+1
    #     # elif i <= (i+(len(Read)/3)) #PARA DIVIDIR A LISTA POR 3
    #     #     ArqThree.append(Reads)
    #     #     i=i+1
    #     else:
    #         ArqTwo.append(Reads) # ESSA LISTA RECEBERÁ Á OUTRA METADE OU 3º TERÇO DO TAMANHO DO CSV
    #         i=i+1
    # df_ArqOne = pd.DataFrame(ArqOne)
    # df_ArqTwo = pd.DataFrame(ArqTwo) 
    # 12 Aug 18 20:11:16  

    # df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
    #                     'B': ['B0', 'B1', 'B2', 'B3'],
    #                     'C': ['C0', 'C1', 'C2', 'C3'],
    #                     'D': ['D0', 'D1', 'D2', 'D3']})



    # df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
    #                     'B': ['B4', 'B5', 'B6', 'B7'],
    #                     'C': ['C4', 'C5', 'C6', 'C7'],
    #                     'D': ['D4', 'D5', 'D6', 'D7']})


    # df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
    #                     'B': ['B8', 'B9', 'B10', 'B11'],
    #                     'C': ['C8', 'C9', 'C10', 'C11'],
    #                     'D': ['D8', 'D9', 'D10', 'D11']})

    # frames = [df1, df2, df3]
    # result = pd.concat(frames)

    #print(jason)

    # print(jason['chave'][1])
    # print(jason['casa'][2])
