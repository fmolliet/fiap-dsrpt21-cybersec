import requests
from bs4          import BeautifulSoup
from urllib.parse import quote

class PasteBin(object):
    
    def __init__(self):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
        }
        
    def __get_source(self, url: str) -> requests.Response:
        return requests.get(url, headers=self.headers)
        
    def crawlRaw(self, query: str ) -> dict:
        response = self.__get_source('https://pastebin.com/raw/%s' % quote(query))
        return response.text