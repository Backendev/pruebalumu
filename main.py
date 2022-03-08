from faulthandler import dump_traceback_later
from fastapi import FastAPI
import time,uvicorn
from config import Config
from singleton import Singleton
from data import Data



class Aplication(metaclass=Singleton):
    def __init__(self):
        self.app = FastAPI(
            title="Prueba Backend Lumu",
            description="Prueba",
            version='1.0.1')
        self.result = {}
        self.data = None


        @self.app.post('/')
        async def index(data):
            self.data_list = Data(data).data_list
            def generator_iter(my_list):
                list_t = my_list
                while len(list_t) > 0:
                    word = list_t[0]
                    len_list_ant = len(list_t)
                    list_t = [i for i in list_t if i != word]
                    self.result[word] = int(len_list_ant) - len(list_t)
                    yield list_t
            for i in generator_iter(self.data_list):
                pass
            print(self.result)
            return self.result

if __name__ == '__main__':
    a = Aplication()
    app = a.app
    c = Config()
    c.run_server(app)
    
