import uvicorn

class Config():
    def __init__(self):
        """
            Configuration for Fast Api Aplication 
            
        """
        self.host = "localhost"
        self.port = 3000
        
    def run_server(self,app):
        """
            Function for run uvicorn server 
            
        """
        uvicorn.run(
            app,
            host=self.host,
            port=self.port
            )