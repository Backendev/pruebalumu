from fastapi import FastAPI
import time,uvicorn
from config import Config
from singleton import Singleton

class Aplication(metaclass=Singleton):
    def __init__(self):
        self.app = FastAPI(
            title="Prueba Backend Lumu",
            description="Prueba",
            version='1.0.1')

        self.result = {}




        @self.app.get('/')
        async def index(word):
            data = """
            lumu lumu lumu lumu lumu illuminates illuminates attacks and adversaries
            lumu illuminates all attacks and adversaries
            lumu illuminates all attacks and adversaries
            """
            data_clean = data.replace('\n',' ')
            data_clean = data_clean.strip()
            data_list = data_clean.split(" ")
            data_list = [i for i in data_list if i != '']
            print(str(data_list))


            def clean_data(function):
                def cleaning(*args,**kwargs):
                    print("__"+str(*args)+str(**kwargs))
                    return function
                return cleaning
            
            
            @clean_data(data)
            def items_iter():
                print("22"+str(data))

            def generator_iter(my_list):
                list_t = my_list
                while len(list_t) > 0:
                    word = list_t[0]
                    len_list_ant = len(list_t)
                    print(len_list_ant)
                    list_t = [i for i in list_t if i != word]
                    print(len(list_t))
                    self.result[word] = int(len_list_ant) - len(list_t)
                    yield list_t
            for i in generator_iter(data_list):
                print(i)
            print(self.result)
            return "Hola"

if __name__ == '__main__':
    a = Aplication()
    app = a.app
    c = Config()
    c.run_server(app)
    
