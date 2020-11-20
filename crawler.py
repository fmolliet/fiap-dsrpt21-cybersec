import requests
from bs4          import BeautifulSoup
from urllib.parse import quote
from PrivateData  import Treated

class GoogleCrawler(object):
    
    types = {
        'file'   : 'filetype',
        'url'    : 'allinrl', 
        'title'  : 'intitle',
        'website': 'site',
        'default': ''
    }
    
    def __init__(self):
        super().__init__()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:79.0) Gecko/20100101 Firefox/79.0',
            'Host': 'www.google.com',
            'Referer': 'https://www.google.com/'
        }
        self.results = []

    def __get_source(self, url: str) -> requests.Response:
        return requests.get(url, headers=self.headers)
        
    def extract_page_results(self, containers):
        for container in containers:
            #obtem os resultados
            title = container.find('h3').text
            url = container.find('a')['href']
            des = container.find('span', class_='aCOpRe').text
            self.results.append({
                'title': title,
                'url': url,
                'description': des
            })

    def search(self, tipe: str, search: str) -> list:
        
        searchType = self.types[tipe]
        
        if self.types[tipe] != '':
            searchType = searchType + ':'
            
        query = searchType + search
    
        # realiza primeira busca
        response = self.__get_source('https://www.google.com/search?q=%s' % quote(query))
        # Inicializa BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
       
        result_pages = soup.select('td > a.fl') 
        
        result_containers = soup.findAll('div', class_='rc')
        
        print('Crawling página: 1')
        
        self.extract_page_results(containers = result_containers)
             
        for num,page in enumerate(result_pages, start=2):
            print('Crawling página: {}'.format(num) )
            
            page_response = self.__get_source('https://www.google.com' + page['href'] )
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            result_containers = soup.findAll('div', class_='rc')
            
            self.extract_page_results(containers = result_containers)
            
            if (num >= len(result_pages)+1):
                soup.select('td > a.fl') 
        
        
        return self.results
