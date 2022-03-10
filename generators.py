import pandas as pd
import re


class Generators:
    @staticmethod
    def generator_iter_mode_1(my_list):
        """
            Function generator iterable Mode 1
            parameters:
            ___________
                        my_list (list): A list to find words
            Returns:
            ___________
                        (tuple) (word (str): word match in list, value (int): number of word searching)
        """
        temp_list = my_list #1
        while len(temp_list) > 0: #n
            word = temp_list[0] #n
            len_list_ant = len(temp_list) #n
            temp_list = [i for i in temp_list if i != word] #n^2
            value = int(len_list_ant) - len(temp_list) #n
            yield word,value 

    def generator_iter_mode_2(my_list):
        """
            Function generator iterable Mode 2
            parameters:
            ___________
                        my_list (list): A list to find words
            Returns:
            ___________
                        (tuple) (word (str): word match in list, value (int): number of word searching)
        """
        temp_list = my_list #1
        while len(temp_list) > 0: #n
            word = temp_list[0] #n
            len_list_ant = len(temp_list) #n
            temp_list = temp_list[1::] #1
            list_to_str = " "+str("  ".join(temp_list))+" " #1
            list_to_str = str(re.sub(r'(\s'+word+'\s)+',"",list_to_str)).strip() #n
            if not len(list_to_str) == 0: #1
                temp_list = list_to_str.replace("  ",",").replace(" ","").split(",") #1
            else: #1
                temp_list = [] #1
            value = int(len_list_ant) - len(temp_list) #n
            yield word,value

    @staticmethod
    def generator_iter_mode_3(my_list):
        """
            Function generator iterable Mode 3
            parameters:
            ___________
                        my_list (list): A list to find words
            Returns:
            ___________
                        (tuple) (word (str): word match in list, value (int): number of word searching)
        """
        temp_list = pd.DataFrame(my_list,columns=["words"]) #1
        while len(temp_list) > 0:#n
            word = temp_list.iloc[0]['words'] #n
            len_list_ant = len(temp_list) #n
            temp_list = temp_list[temp_list['words'] != word ].reset_index(drop=True) #n^2
            value = int(len_list_ant) - len(temp_list)  #n
            yield word,value
    
    
    