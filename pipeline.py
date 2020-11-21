import re

from crawler         import GoogleCrawler
from PastebinCrawler import PasteBin
from PrivateData     import Treated
class Pipeline(object):
    
    def __init__(self, type: str, query: str ) -> None:
        super().__init__()
        self.expr   = re.compile('/([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)/')
        self.type   = type
        self.founds = []
        self.raw    = GoogleCrawler().search(type, query)
        
    def struct_data(self) -> dict :
        
        for key in self.raw:
            title = key.get("title")
            url   = key.get("url")
            conteudo = key.get("description")
            
            if ( url.find('pastebin') ): 
                link = url.replace("https://pastebin.com/", "").replace("raw/","")
                
                content = PasteBin().crawlRaw(link)
                
                
                self.founds.append(
                    Treated('pastebin_raw', url, '', content).get_data()
                )
            
            if (self.expr.match(conteudo)):
                self.founds.append(
                    Treated('email_google', url, '', conteudo).get_data()
                )
            
            self.founds.append(
                    Treated(self.type, url, title, conteudo).get_data()
                )
                
        return self.founds