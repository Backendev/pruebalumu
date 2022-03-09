from fastapi import FastAPI, HTTPException
import uvicorn,re
from datetime import datetime
from config import Config
from singleton import Singleton
from data import Data
from generators import Generators as gen



class Aplication(metaclass=Singleton):
    """
        Function fastApi Aplication generate
        
    """
    def __init__(self):
        self.app = FastAPI(
            title="Prueba Backend Lumu",
            description="Prueba",
            version='1.0.1')
        self.result = {}
        self.data = None
        self.sorted_result = {}


        @self.app.post('/')
        async def index(data,mode=1):
            """
                Function generator iterable Mode 1
                parameters:
                ___________
                            data (str): A string whit words separate whit comas
                            mode (int): Mode to strategy for create generator
                Returns:
                ___________
                            (dict) result: Dictionary {keys:word match,values: number of coincidences}
            """
            
            if len(data) > 0 or data == None:
                self.data_list = Data(data).data_list
                if mode == "1":
                    self.generator_mode_1() #n
                if mode == "2":
                    self.generator_mode_2() #n^2
                if mode == "3":
                    self.generator_mode_3() #n^2
                sorted_result = Data.sorted_values(self.result) #n
                self.sorted_result = { k:self.result[k] for k in sorted_result } #n
                return self.sorted_result
            else:
                raise HTTPException(status_code=404, detail="Invalid data")
    
    def generator_mode_1(self):
        for w,v in gen.generator_iter_mode_1(self.data_list):
            self.result[w] = v
        
    
    def generator_mode_2(self):
        for w,v in gen.generator_iter_mode_2(self.data_list):
            self.result[w] = v

    
    def generator_mode_3(self):
        for w,v in gen.generator_iter_mode_3(self.data_list):
            self.result[w] = v




if __name__ == '__main__':
    a = Aplication()
    app = a.app
    c = Config()
    c.run_server(app)
    
