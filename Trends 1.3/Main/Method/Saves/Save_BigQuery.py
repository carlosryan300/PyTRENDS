import gspread, csv, os, sys, time, os.path as path, pandas as pd

PATH = os.getcwd()
def Save_BigQuery(KeyWordRead, Arq, Index, Date):
    try:
        HeadExcel = pd.read_excel("{0}/FILES/Excel/{1}".format(PATH, Arq))
        for KeyWordReads in KeyWordRead:
            print("    DATE           VALOR ")
            for index, linhas in HeadExcel.iterrows():
                print(linhas[Index], linhas[KeyWordReads], Date, sep="|")
    except Exception as Erro:
        print("def Save_BigQuery -> Ocorreu o Erro:{0}".format(Erro))