import socket, time, math
i = 60
URLCONFIAVEIS = ["www.google.com", "www.uol.com", "www.amazon.com" ]
def Check_Connection():
    global URLCONFIAVEIS
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
def Valida_Connection():

    check = False
    while check==False:
        if Check_Connection()==True:
            check=True
            pass
        else:
            print("..Opss! NÃO HÁ CONEXÃO COM A INTERNET, POR FAVOR VERIFIQUE A CONEXÃO!..")
            print("================EM {0} MIN TENTAREI EXECUTAR NOVAMENTE!================".format(math.trunc(i/60)))
            time.sleep(i)
            i = i+60

