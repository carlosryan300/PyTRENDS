import pandas as pd, os.path as path
import gspread, openpyxl
from datetime import date, datetime
from oauth2client.service_account import ServiceAccountCredentials
import subprocess
import sys, time, os
PATH = os.getcwd()
def Write_Excel(df_save, Name):
    print('Write_Excel')
    df = pd.DataFrame(df_save)
    df.to_excel(PATH+'/CSV/{}'.format(Name), index=False)

def Read_Tail(Name):
    print('Read_Tail')
    pd_read = pd.read_excel(PATH+'/CSV/{}'.format(Name))
    df_line = pd.DataFrame(pd_read).tail(1)
    x = ''
    for index, i in df_line.iterrows():
        x = i[0]
    return str(x)

def GSheet():
    print('GSheet')
    escopo =  ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(PATH+'/json/bot_whp.json', escopo)
    autorizacao = gspread.authorize(credenciais)
    sheets = autorizacao.open("rotinas").worksheet("Trends_Rotinas")
    Rotina = {
        'cale':sheets.acell('E3').value,
        'hora':sheets.acell('F3').value
    }
    return Rotina 

def Controle():
    print('Controle')
    print("Data de Count_Date_Day")
    Create_Rotina = GSheet()
    Name = str(Create_Rotina['cale']+'.xlsx')
    Periodo = Create_Rotina['cale']

    if path.isfile(Name)==True:
        if Periodo == 'Diario':
            pass
        else:
            Count_Date = Read_Tail(Name).replace(Create_Rotina['cale']+' ', '')
            print(Count_Date)
            if Count_Date_Day(Count_Date, Create_Rotina['cale'])==True:
                pass
            else:
                sys.exit()

    concatenar = '{} {} {}'.format(Create_Rotina['cale'], date.today(), Create_Rotina['hora'])

    if Periodo == 'Diario':
        return Create_Rotina['hora']
    elif path.isfile(Name)==True:
        if concatenar == Read_Tail(Name):
            print('Já Exixte')
            return "Já existe"
        else:
            print('Não Existe')
            Write_Excel([concatenar], Name)
            return Create_Rotina['hora']
    else:
        Write_Excel([concatenar], Name)
        return Create_Rotina['hora']

def Convert_Date_Str(date_e_time_agend):
    print('Convert_Date_Str')
    date_e_time_atual = time.strftime('%Y-%m-%d %H:%M:%S')
    date_e_time_formt = '%Y-%m-%d %H:%M:%S'
    Seconde = (datetime.strptime(date_e_time_agend, date_e_time_formt) - datetime.strptime(date_e_time_atual, date_e_time_formt)).total_seconds()
    return int(Seconde)

def Count_Date_Day(Count_Date, Periodo):
    print('Count_Date_Day')
    print("Count_Date_Day")
    hj = date.today()
    Date_e_time_formt = '%Y-%m-%d %H:%M:%S'
    Convert_Data =  (hj.toordinal()-datetime.strptime(Count_Date, Date_e_time_formt).toordinal())
    print("Data de Count_Date_Day"+str(Count_Date))
    print("Data de Count_Date_Day"+str(hj))
    print(Convert_Data)

    if Periodo == 'Diario':
        return True
    elif Periodo == "Semanal" and Convert_Data == 7:
        return True
    elif Periodo == "Mensal" and Convert_Data >= 29 and Convert_Data <= 31:
        return True
    else:
        sys.exit()

def Sitution(Value):
    escopo = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credenciais = ServiceAccountCredentials.from_json_keyfile_name(PATH+"/json/bot_whp.json", escopo)
    autorizacao = gspread.authorize(credenciais)
    sheet = autorizacao.open('rotinas').worksheet('Trends_Rotinas')
    sheet.update_acell('G3', Value)
def Verificador():
    print('Verificador')
    Opcao = Controle()
    if Opcao == "Já existe":
        print("existe")
        sys.exit()
    else:
        date_e_time_agend = '{0} {1}'.format(time.strftime('%Y-%m-%d'), Opcao)
        print(date_e_time_agend)
        Sleep_Second = Convert_Date_Str(date_e_time_agend)
        if Sleep_Second >= 0:
            print('data ok')
            print(Sleep_Second)
            print('Programa Dormindo')
            time.sleep(Sleep_Second-10)
            subprocess.call('bash script_exec.sh', shell=True)
            Sitution('Em Execução')
            time.sleep(10)
            sys.exit()
        else:
            print('data inválida')
            Sitution('Data Inválida')
            sys.exit()

Verificador()