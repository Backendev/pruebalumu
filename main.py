from fastapi import FastAPI, HTTPException
import uvicorn,re
from datetime import datetime
from config import Config
from data import Data
from generators import Generators as gen



class Aplication():
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
                Endpoint unique path 
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
                    self.generator_mode_1() #n^2
                elif mode == "2":
                    self.generator_mode_2() #n^2
                elif mode == "3":
                    self.generator_mode_3() #n^2
                else:
                    raise HTTPException(status_code=404, detail="Invalid mode, modes: 1,2 or 3")
                sorted_result = Data.sorted_values(self.result) #n
                self.sorted_result = list(map(lambda x: {"word":x,"count":self.result[x]},sorted_result))#n
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
    
