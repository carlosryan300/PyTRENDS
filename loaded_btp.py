#import necessárias
import json
import math
import pprint
import socket
import sys
import os
import csv
import time
import gspread
import requests
import oauth2client.service_account
import subprocess

URLConfiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
CountRepeat = 1
p=False

def ChecaConexao():
   global URLConfiaveis
   for urlconfiaveis in URLConfiaveis:
     a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     a.settimeout(.5)
     try:
       b=a.connect_ex((urlconfiaveis, 80))
       if b==0: #ok, conectado
         return True

     except:
       pass
     a.close()
   return False

def TesteWebPage(): 
    cssBytes=[]
    flashBytes=[]
    fontBytes=[]
    htmlBytes=[]
    imageBytes=[]
    jsBytes=[]
    otherBytes=[]
    cssBytesUncompressed=[]
    flashBytesUncompressed=[]
    fontBytesUncompressed=[]
    htmlBytesUncompressed =[]
    imageBytesUncompressed=[]
    jsBytesUncompressed=[]
    otherBytesUncompressed=[]
    cssrequests=[]
    flashrequests=[]
    fontrequests=[]
    htmlrequests=[]
    imagerequests=[]
    jsrequests=[]
    otherrequests=[] 
    Binario = False  
    CountResult = 0
    CountCable = 0
    Count3GSlow = 0
    CountKey = 0
    CountFim = 0
    tempo = 0  
    ArmJson = []
    SpeedIndex = []
    FullyLoaded = []
    From = ""
    TestUrl = []
    Completed = []
    Connectivity = []
    caminho = os.getcwd()
    API_KEY = {"key":[
        "A.5e2e8cafd9fc6578e666886acff8f8ae"
    ]
    }
    UrlSite = {"URL":[ 
        "http://www.brastemp.com.br"

    ]  
    }  
    TipoTest = {"Tipo":[ 
        "3GSlow",
        "Cable"    
    ]  
    } 
    while CountFim < len(TipoTest["Tipo"]): 
        if (TipoTest["Tipo"][CountFim])=="Cable":
            while CountCable < len(UrlSite["URL"]):
                ShowURL = UrlSite["URL"][CountCable] 
                TrocaKey = API_KEY["key"][CountKey]     
                UrlWebPage = "http://www.webpagetest.org/runtest.php?k={0}&url={1}&breakdown=1&runs=1&fvonly=0&f=json&location=SaoPaulo_BR:Chrome.Cable".format(TrocaKey, ShowURL)
                Retorno = requests.api.get(UrlWebPage).json()
                if (Retorno['statusText'])=="The test request will exceed the daily test limit for the given API key":
                    CountKey = CountKey+1
                    if CountKey >= len(API_KEY["key"]):
                        CountKey=0
                else:
                    #pass    
                    JsonUrl = (Retorno['data']['jsonUrl'])                
                    CountCable = CountCable+1          
                    CountKey = CountKey+1
                    if CountKey >= len(API_KEY["key"]):
                        CountKey=0
                    ArmJson.append(JsonUrl)
            print("O STATUS DE TESTE DE CABLE ESTÁ COMO: {0}".format(Retorno["statusText"]))       
            CountFim = CountFim+1
            CountKey = 0
        elif (TipoTest["Tipo"][CountFim])=="3GSlow":
            while Count3GSlow < len(UrlSite["URL"]):
                ShowURL = UrlSite["URL"][Count3GSlow]  
                TrocaKey = API_KEY["key"][CountKey]            
                UrlWebPage = "http://www.webpagetest.org/runtest.php?k={0}&url={1}&breakdown=1&runs=1&fvonly=0&f=json&location=SaoPaulo_BR:Chrome.3GSlow".format(TrocaKey, ShowURL) 
                Retorno = requests.api.get(UrlWebPage).json()
                if (Retorno['statusText'])=="The test request will exceed the daily test limit for the given API key":
                    CountKey = CountKey+1
                    if CountKey >= len(API_KEY["key"]):
                        CountKey=0
                else:
                    #pass    
                    JsonUrl = (Retorno['data']['jsonUrl'])                
                    Count3GSlow = Count3GSlow+1          
                    CountKey = CountKey+1
                    if CountKey >= len(API_KEY["key"]):
                        CountKey=0
                    ArmJson.append(JsonUrl)
            print("O STATUS DE TESTE DE 3G ESTÁ COMO: {0}".format(Retorno["statusText"]))       
            CountFim = CountFim+1
            CountKey = 0
    print("\n")
    print("==================== TESTE DE EXTRAÇÃO DE URLs CONCLUÍDO COM SUCESSO. =========================")
    pprint.pprint("URLs: {0}".format(ArmJson))

    iBackup = 0
    for Arm in ArmJson:
        t = str(time.strftime('%d %b %y %H:%M:%S'))
        with open('{0}/UrlBackup/URLsTest.txt'.format(caminho), 'a', newline="") as backup:
            backup.write("URL: {0} - Data e Hora: {1} \n".format(str(ArmJson[iBackup]),t))
            backup.close()
            iBackup=iBackup+1
    while CountResult < len(ArmJson): 
        i = 0 
        if Binario == False:
            tamanho = len(ArmJson)-1  
            Verificador0 = ArmJson[tamanho]
            Verificador1 = requests.api.get(Verificador0).json()
            Verificador2 = json.dumps(Verificador1['data']["statusCode"])
            print("=============================POR FAVOR AGUARDE O TESTE ACABAR==================================")
            if Verificador2 !='200':
                try:
                    while (Verificador2)!='200':
                        check = False
                        try:
                            while check==False:
                                if ChecaConexao()==True:
                                    check=True
                                    pass
                                elif ChecaConexao()==False:
                                    print("...............OPS! NÃO HÁ CONEXÃO COM A INTERNET, POR FAVOR VERIFIQUE A CONEXÃO!..............")
                                    print("======================== EM UM MINUTO TENTAREI EXECUTAR NOVAMENTE =============================")
                                    time.sleep(60) 
                        except Exception as Falha:
                            print("Falha:{0}".format(Falha))
                            continue
                        tamanho = len(ArmJson)-1 
                        Verificador0 = ArmJson[tamanho]
                        Verificador1 = requests.api.get(Verificador0).json()
                        Verificador2 = json.dumps(Verificador1["statusCode"])
                        while i < 60:          
                            time.sleep(1)
                            i=i+1
                        tempo = tempo+i
                        i=0
                    print("MINUTOS:{0} ".format(math.trunc(tempo/60)))              
                         
                    Binario = True  
                except Exception as Error:
                    print("OCORREU O ERROR:{}".format(Error))
                    pass
            else:
                pass
        elif Binario == True:
            pass         
        JsonResult = requests.api.get(ArmJson[CountResult]).json()
        #OTHERS
        try:
            if int(json.dumps(JsonResult['data']["successfulFVRuns"]))>=1:
                SiteTest = (json.dumps((JsonResult['data']['testUrl']), indent=2))
                SpeedIndex = (json.dumps((JsonResult['data']['average']['firstView']['SpeedIndex']),indent=2))
                FullyLoaded = (json.dumps((JsonResult['data']['average']['firstView']['fullyLoaded']),indent=2))
                if len(FullyLoaded) == 6:
                    seg = FullyLoaded[:3]
                    cent = FullyLoaded[3:]
                    FullyLoaded = (seg +'.'+cent)
                elif len(FullyLoaded) == 5:
                    seg = FullyLoaded[:2]
                    cent = FullyLoaded[2:]
                    FullyLoaded = (seg +'.'+cent)
                elif len(FullyLoaded) == 4:
                    seg = FullyLoaded[:1]
                    cent = FullyLoaded[3:]
                    FullyLoaded = (seg +'.'+cent)    
                else:
                    pass
                From = (json.dumps((JsonResult['data']['from']), indent=2))
                TestUrl = (json.dumps((JsonResult['data']['summary']), indent=2))
                Completed = (time.strftime('%d %b %y %H:%M:%S'))
                Connectivity = (json.dumps((JsonResult['data']['connectivity']), indent=2))
                #BYTES
                cssBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["css"]["bytes"])        
                flashBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["flash"]["bytes"])
                fontBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["font"]["bytes"])
                htmlBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["html"]["bytes"])
                imageBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["image"]["bytes"])
                jsBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["js"]["bytes"])
                otherBytes = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["other"]["bytes"])
                #BytesUncompressed
                cssBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["css"]["bytesUncompressed"])
                flashBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["flash"]["bytesUncompressed"])
                fontBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["font"]["bytesUncompressed"])
                htmlBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["html"]["bytesUncompressed"])
                imageBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["image"]["bytesUncompressed"])
                jsBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["js"]["bytesUncompressed"])
                otherBytesUncompressed = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["other"]["bytesUncompressed"])
                #REQUESTS
                cssrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["css"]["requests"])
                flashrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["flash"]["requests"])
                fontrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["font"]["requests"])
                htmlrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["html"]["requests"])
                imagerequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["image"]["requests"])
                jsrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["js"]["requests"])
                otherrequests = json.dumps(JsonResult["data"]["runs"]["1"]["firstView"]["breakdown"]["other"]["requests"])
                
                escopo =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
                credenciais = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name('{0}/json/bot-carregamento-whp.json'.format(caminho), escopo)
                autorizacao = gspread.authorize(credenciais)
                sheet =  autorizacao.open("btp_institucional").sheet1
                sheet.append_row([SiteTest.replace('"',''), int(SpeedIndex), float(FullyLoaded), From[1:18].replace('"',''), TestUrl.replace('"',''), Completed.replace('"',''), Connectivity.replace('"',''), math.trunc(tempo/60),  int(cssBytes), int(flashBytes), int(fontBytes), int(htmlBytes), int(imageBytes),  int(jsBytes), int(otherBytes), int(cssBytesUncompressed), int(flashBytesUncompressed),  int(fontBytesUncompressed), int(htmlBytesUncompressed), int(imageBytesUncompressed),  int(jsBytesUncompressed), int(otherBytesUncompressed), int(cssrequests), int(flashrequests),  int(fontrequests), int(htmlrequests), int(imagerequests), int(jsrequests), int(otherrequests)])
                
                os.makedirs("{0}/CSV/".format(caminho), exist_ok=True)
                    
                if os.path.isfile("{0}/CSV/Bot_Web_Page.csv".format(caminho))==False:
                    with open('{0}/CSV/Bot_Web_Page.csv'.format(caminho), 'a', newline="", encoding="utf-8") as f:
                        try:
                            writer = csv.writer(f, delimiter=";")
                            writer.writerow(("Site Testado", "SpeedIndex	", "FullyLoaded", "Local", "URLTest", "Data e Hora", "Tipo de Teste", "Tempo Estimado.Minutos", "cssBytes",	 "flashBytes", "fontBytes", "htmlBytes", "imageBytes", "jsBytes", "otherBytes", "cssBytesUncompressed", "flashBytesUncompressed", "fontBytesUncompressed", "htmlBytesUncompressed", "imageBytesUncompressed", "jsBytesUncompressed", "otherBytesUncompressed", "cssrequests", "flashrequests", "fontrequests", "htmlrequests", "imagerequests", "jsrequests", "otherrequests"))
                            writer.writerow([SiteTest.replace('"',''), int(SpeedIndex), float(FullyLoaded), From[1:18].replace('"',''), TestUrl.replace('"',''), Completed.replace('"',''), Connectivity.replace('"',''), math.trunc(tempo/60),  int(cssBytes), int(flashBytes), int(fontBytes), int(htmlBytes), int(imageBytes),  int(jsBytes), int(otherBytes), int(cssBytesUncompressed), int(flashBytesUncompressed),  int(fontBytesUncompressed), int(htmlBytesUncompressed), int(imageBytesUncompressed),  int(jsBytesUncompressed), int(otherBytesUncompressed), int(cssrequests), int(flashrequests),  int(fontrequests), int(htmlrequests), int(imagerequests), int(jsrequests), int(otherrequests)])
                        finally:
                            f.close()
                else:
                    with open('{0}/CSV/Bot_Web_Page.csv'.format(caminho), 'a', newline="", encoding="utf-8") as f:
                        try:
                            writer = csv.writer(f, delimiter=";")
                            writer.writerow([SiteTest.replace('"',''), int(SpeedIndex), float(FullyLoaded), From[1:18].replace('"',''), TestUrl.replace('"',''), Completed.replace('"',''), Connectivity.replace('"',''), math.trunc(tempo/60),  int(cssBytes), int(flashBytes), int(fontBytes), int(htmlBytes), int(imageBytes),  int(jsBytes), int(otherBytes), int(cssBytesUncompressed), int(flashBytesUncompressed),  int(fontBytesUncompressed), int(htmlBytesUncompressed), int(imageBytesUncompressed),  int(jsBytesUncompressed), int(otherBytesUncompressed), int(cssrequests), int(flashrequests),  int(fontrequests), int(htmlrequests), int(imagerequests), int(jsrequests), int(otherrequests)])
                        finally:
                            f.close()
                CountResult = CountResult+1
            elif int(json.dumps(JsonResult['data']["successfulRVRuns"]))==0 and int(json.dumps(JsonResult['data']["successfulFVRuns"]))==0:
                print("O TESTE DA URL: {0}, FOI INVÁLIDO OU NÃO OBTEVE SUCESSO".format(json.dumps(JsonResult['data']['summary']), indent=2))
                CountResult = CountResult+1 
            else:
                print("O TESTE DA URL: {0}, FOI INVÁLIDO OU NÃO OBTEVE SUCESSO".format(json.dumps(JsonResult['data']['summary']), indent=2))
                CountResult = CountResult+1 
        except Exception as Erro:
            print("OCORREU O ERROR:{}".format(Erro))
            CountResult = CountResult+1 
            subprocess.check_output(['bash', '-c', 'echo "OCORREU O ERROR: {0}" | mail -s "SCRIPT LOADED BTP" carlos.silva@jussi.com.br'.format(erro)])
            continue                      
sina = 5

while CountRepeat < sina:   
    TesteWebPage()    
    print("========================== FOI FEITO O {0}º TESTE COM SUCESSO =================================".format(CountRepeat))   
    CountRepeat=CountRepeat+1  


print("<><><><><><><><><><><><><><><><><>< TESTES FINALIZADOS ><><><><><><><><><><><><><><<><><><><><>") 
