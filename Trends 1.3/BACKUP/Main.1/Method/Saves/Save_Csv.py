import pandas as pd, os, time, pprint
from Saves.Save_GSheets import PrepareList
Local = os.getcwd()
i = 1
class Save_Csv():

    def __init__():
        pass
    def Create_List(Path, ListValue):       
        if os.path.isfile(Path)==True: 
            Read = pd.read_csv(Path)
            df_Read = pd.DataFrame(Read)
            df_ListValue =pd.DataFrame(ListValue)
            df_Frame = [df_Read, df_ListValue]
            df_Save = pd.concat(df_Frame)
            df_Save.to_csv(Path, index=False)
        else:    
            df = pd.DataFrame(ListValue)
            df.to_csv(Path , index=False)
 
    def SaveRelated(ListValue, Name):
        if os.path.isfile(Name)==True:
            Read = pd.read_csv(Name)
            df_Exist = pd.DataFrame(Read)
            df_New = pd.DataFrame(ListValue)
            frames = [Read, df_New]
            result = pd.concat(frames)
            result.to_csv(Name, index=False)
        else:
            df_Save = pd.DataFrame(ListValue)
            df_Save.to_csv(Name, index=False)

    # def SaveNew(self, ListValue):
    #     if os.path.isfile(self)==True:
    #         df_ListValue = pd.DataFrame(ListValue)
    #         df_Exist = pd.read_csv(self)
    #         df_Frame = [df_Exist, df_ListValue]
    #         df_Save = pd.concat(df_Frame)
    #         df_Save.to_csv(self, index=False)
    #     else:
    #         df_ListValue = pd.DataFrame(ListValue)
    #         df_ListValue.to_csv(self, index=False)


    def PrepareValue(List, ColumnOne, NameTable, KeyWord, self):
        Time = time.strftime("%d/%m/%Y %H:%M")
        global i
        Local = os.getcwd()+'/FILES/Excel/{0}.csv'.format(NameTable)
        ListData = {
            '{0}'.format(ColumnOne):[],
            'values':[],
            'Termo Buscado':[],
            'Data e Hora':[],
            'Palavra Pivo':[],
            'Num da Comp':[],
            'Periodo':[]
        }
        
        ListValue = pd.DataFrame(List)
        for KWords in KeyWord:
            for index,Reads in ListValue.iterrows():
                ListData['{0}'.format(ColumnOne)].append(Reads[ColumnOne])
                ListData['values'].append(Reads[KWords])
                ListData['Termo Buscado'].append(KWords)
                ListData['Data e Hora'].append(Time)
                ListData['Palavra Pivo'].append(KeyWord[0])
                ListData['Num da Comp'].append("{0}º".format(i))
                ListData['Periodo'].append(self)
        i = i+1
        Save_Csv.Create_List(Local, ListData)    

