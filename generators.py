import re,time
import pandas as pd
from data import Data as da

class Generators:
    


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
        temp_list = my_list
        while len(temp_list) > 0:
            word = temp_list[0]
            len_list_ant = len(temp_list)
            temp_list = da.generate_new_list(temp_list,word)
            value = int(len_list_ant) - len(temp_list)
            yield word,value
    
    @staticmethod
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
        temp_list = my_list
        while len(temp_list) > 0:
            word = temp_list[0]
            len_list_ant = len(temp_list)
            temp_list = [i for i in temp_list if i != word]
            value = int(len_list_ant) - len(temp_list) 
            yield word,value
    
    
    @staticmethod
    def generator_iter_mode_3(my_list):
        """
            Function generator iterable Mode 2
            parameters:
            ___________
                        my_list (list): A list to find words
            Returns:
            ___________
                        (tuple) (word (str): word match in list, value (int): number of word searching)
        """
        temp_list = pd.DataFrame(my_list,columns=["words"])
        while len(temp_list) > 0:
            word = temp_list.iloc[0]['words']
            len_list_ant = len(temp_list)
            temp_list = temp_list[temp_list['words'] != word ].reset_index(drop=True)
            value = int(len_list_ant) - len(temp_list) 
            yield word,value