import uvicorn
from singleton import Singleton

class Config(metaclass=Singleton):
    def __init__(self):
        self.host = "localhost"
        self.port = 8000
        self.log_level="info"
        self.reload = True
        self.workers = "2"
    def run_server(self,app):
        uvicorn.run(
            app,
            host=self.host,
            port=self.port
            )