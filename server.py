from crawler import GoogleCrawler
from pprint import pprint

if __name__ == '__main__':
    pprint(GoogleCrawler().search(input('Quer buscar oque? ')))