import pandas as pd, os, time
#from Validation.Method.List_KeyWord import KeyWords
Local = os.getcwd()

Time = time.strftime("%d/%m/%Y %H:%M")

class Save_Csv():

    def __init__():
        pass
    def Create_List(Path, ColumnOne, ColumnTwo, NewFile, KeyWord, self):
        Read = pd.read_excel(Path)
        i = 1
        global Time
        global ListValue
        ListValue = {
            '{0}'.format(ColumnOne):[],
            '{0}'.format(ColumnTwo):[],
            'Termo Buscado':[],
            'Data e Hora':[],
            'Palavra Pivo':[],
            'Num da Comp':[],
            'Periodo':[]
        }
        
        for KWords in KeyWord:
            for index,Reads in Read.iterrows():
                ListValue['{0}'.format(ColumnOne)].append(Reads[ColumnOne])
                ListValue['{0}'.format(ColumnTwo)].append(Reads[KWords])
                ListValue['Termo Buscado'].append(KWords)
                ListValue['Data e Hora'].append(Time)
                ListValue['Palavra Pivo'].append(KeyWord[0])
                ListValue['Num da Comp'].append("{0}º".format(i))
                ListValue['Periodo'].append(self)
        i = i+1
        if os.path.isfile(NewFile)==True: 
            ReadExist = pd.read_excel(NewFile)
            for index,ReadExists in ReadExist.iterrows():
                ListValue['{0}'.format(ColumnOne)].append(ReadExists[ColumnOne])
                ListValue['{0}'.format(ColumnTwo)].append(ReadExists["values"])
                ListValue['Termo Buscado'].append(ReadExists['Termo Buscado'])
                ListValue['Data e Hora'].append(ReadExists['Data e Hora'])
                ListValue['Palavra Pivo'].append(ReadExists['Palavra Pivo'])
                ListValue['Num da Comp'].append(ReadExists['Num da Comp'])
        else:
            pass
        df = pd.DataFrame(ListValue)
        df.to_excel(NewFile , index=False)

    def SaveRelated(ListValue, Name):
        if os.path.isfile(Name)==True:
            Read = pd.read_excel(Name)
            df_Exist = pd.DataFrame(Read)
            df_New = pd.DataFrame(ListValue)
            frames = [Read, df_New]
            result = pd.concat(frames)
            result.to_excel(Name, index=False)
        else:
            df_Save = pd.DataFrame(ListValue)
            df_Save.to_excel(Name, index=False)






