class Data:
    def __init__(self,data):
        self.__data = data
        self.__data_list = self.get_data_list()

    def get_data_list(self):
        if "\n" in self.__data:
            data_clean = self.__data.replace('\n',' ').strip()
            data_list = data_clean.split(" ")
            data_list = [i for i in data_list if i != '']
        else:
            data_list = self.__data.split(" ")
        return data_list

    
    @property
    def data_list(self):
        return self.__data_list