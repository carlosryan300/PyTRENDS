import pandas as pd, os, time
Local = os.getcwd()
class Save_Csv():

    def __init__():
        pass
    def Create_List(Path, ColumnOne, ColumnTwo, NewFile, KeyWord):
        Read = pd.read_excel(Path)
        Time = time.strftime("%d/%m/%Y %H:%M")
        ListValue = {
            '{0}'.format(ColumnOne):[],
            '{0}'.format(ColumnTwo):[],
            'Termo Buscado':[],
            'Data e Hora':[]
        }
        for KeyWords in KeyWord:
            for index,Reads in Read.iterrows():
                ListValue['{0}'.format(ColumnOne)].append(Reads[ColumnOne])
                ListValue['{0}'.format(ColumnTwo)].append(Reads[KeyWords])
                ListValue['Termo Buscado'].append(KeyWords)
                ListValue['Data e Hora'].append(Time)
        if os.path.isfile(NewFile)==True: 
            ReadExist = pd.read_excel(NewFile)
            for index,ReadExists in ReadExist.iterrows():
                ListValue['{0}'.format(ColumnOne)].append(ReadExists[ColumnOne])
                ListValue['{0}'.format(ColumnTwo)].append(ReadExists["values"])
                ListValue['Termo Buscado'].append(ReadExists['Termo Buscado'])
                ListValue['Data e Hora'].append(ReadExists['Data e Hora'])
        else:
            pass
        df = pd.DataFrame(ListValue)
        df.to_excel(NewFile)