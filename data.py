import re

class Data:
    def __init__(self,data):
        self.__data = data
        self.__data_list = self.get_data_list()

    def get_data_list(self):
        """
            Generate List to String data
            Return:
            _______
                    data_list (list): List whit words to data
        """
        if "\n" in self.__data:
            data_clean = self.__data.replace('\t',' ').strip() #1
            data_clean = self.__data.replace('\n',' ').strip() #1
            data_list = data_clean.split(" ") #1
            data_list = [i for i in data_list if i != ''] #n
        else:
            data_list = self.__data.split(" ") #1
            data_list = [i for i in data_list if i != ''] #n
        return data_list

    
    @property
    def data_list(self):
        return self.__data_list

    @staticmethod
    def generate_new_list(temp_list,word):
        temp_list = temp_list[1::] #1
        list_to_str = " "+str("  ".join(temp_list))+" " #1
        list_to_str = str(re.sub(r'(\s'+word+'\s)+',"",list_to_str)).strip() #1
        if not len(list_to_str) == 0: #1
            temp_list = list_to_str.replace("  ",",").replace(" ","").split(",") #1
        else: #1
            temp_list = [] #1
        return temp_list #1


    @staticmethod
    def sorted_values(dic):
        def particion(lista, izq, der):
            pivote = dic[lista[der]] #1
            indice = izq #1
            for i in range(izq, der): #n
                if dic[lista[i]] >= pivote: #n
                    lista[indice], lista[i] = lista[i], lista[indice] #n
                    indice += 1 #n
            lista[indice], lista[der] = lista[der], lista[indice] #1
            return indice

        def quicksort(lista, izq, der):
            if izq < der: #1
                pivote_indice = particion(lista, izq, der) #n
                quicksort(lista, izq, pivote_indice-1)#n
                quicksort(lista, pivote_indice+1, der)#n
        lista = list(dic.keys())#1
        quicksort(lista, 0, len(lista)-1)#1
        return lista

