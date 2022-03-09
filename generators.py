import re

class Generators:
    @staticmethod
    def generator_iter_mode_1(my_list):
        list_t = my_list
        while len(list_t) > 0:
            word_h = list_t[0]
            len_list_ant = len(list_t)
            list_t = list_t[1::]
            list_to_str = "  ".join(list_t)
            list_to_str = " "+str(list_to_str)+" "
            patron = r'(\s'+word_h+'\s)+'
            list_to_str = re.sub(patron,"",list_to_str)
            list_to_str = list_to_str.strip()
            if not len(list_to_str) == 0:
                list_to_str = list_to_str.replace("  ",",").replace(" ","")
                list_t = list_to_str.split(",")
            else:
                list_t = []
            value = int(len_list_ant) - len(list_t)
            yield word_h,value
    
    @staticmethod
    def generator_iter_mode_2(my_list):
        list_t = my_list
        while len(list_t) > 0:
            word_h = list_t[0]
            len_list_ant = len(list_t)
            list_t = [i for i in list_t if i != word_h]
            value = int(len_list_ant) - len(list_t)
            yield word_h,value