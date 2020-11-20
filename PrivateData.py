from datetime import datetime

class Treated(object):
    
    def __init__(self, tipo: str, source: str, business: str, content: str ,relevancia) -> None:
        super().__init__()
        self.data       = datetime.now()
        self.tipo       = tipo
        self.fonte      = source
        self.content    = content
        self.empresa    = business
        self.relevancia = relevancia
        
    def get_data(self) -> dict:
        return { 
            'tipo'       : self.tipo,
            'fonte'      : self.fonte,
            'content'    : self.content,
            'empresa'    : self.empresa,
            'relevancia' : self.relevancia,
            'data'       : self.data
        }