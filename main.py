from fastapi import FastAPI, HTTPException
import time,uvicorn,re
from config import Config
from singleton import Singleton
from data import Data
from generators import Generators as gen



class Aplication(metaclass=Singleton):
    def __init__(self):
        self.app = FastAPI(
            title="Prueba Backend Lumu",
            description="Prueba",
            version='1.0.1')
        self.result = {}
        self.data = None
        self.alg_complex = {'1':0,'2':0}


        @self.app.post('/')
        async def index(data,mode=1):
            print("Mode "+str(mode))
            if len(data) > 0:
                self.data_list = Data(data).data_list
                


                print(str(type(self.data_list)))
                if mode == "1":
                    for w,v in gen.generator_iter_mode_1(self.data_list):
                        self.result[w] = v
                if mode == "2":
                    for w,v in gen.generator_iter_mode_2(self.data_list):
                        self.result[w] = v
                print(self.result)
                return self.result
            else:
                raise HTTPException(status_code=404, detail="Invalid data")

if __name__ == '__main__':
    a = Aplication()
    app = a.app
    c = Config()
    c.run_server(app)
    
