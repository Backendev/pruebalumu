import re


class Data():
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
            data_list = self.__data.strip().split(" ") #1
        return data_list

    
    @property
    def data_list(self):
        return self.__data_list

    @staticmethod
    def sorted_values(dic):
        """
            Sorted Function to list 
            Parameters:
            _______
                    dic (dict): Dict whit results
        """
        def partition(res_list, left, right):
            pivot = dic[res_list[right]] #1
            index = left #1
            for i in range(left, right): #n
                if dic[res_list[i]] >= pivot: #n
                    res_list[index], res_list[i] = res_list[i], res_list[index] #n
                    index += 1 #n
            res_list[index], res_list[right] = res_list[right], res_list[index] #1
            return index

        def quicksort(res_list, left, right):
            if left < right: #1
                pivot_i = partition(res_list, left, right) #n^2
                quicksort(res_list, left, pivot_i-1)#n
                quicksort(res_list, pivot_i+1, right)#n
        res_list = list(dic.keys())#1
        quicksort(res_list, 0, len(res_list)-1)#1
        return res_list
    

