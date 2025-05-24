import requests as r
from bs4 import BeautifulSoup as bs

url = 'https://uol.com.br/start/esport'
page = r.get(url)

soup = bs(page.content, 'html.parser')

lista = ['casimiro']

for paragrafo in soup.find_all('body'):
    for palavra in lista:
        for paragrafo_str in paragrafo.stripped_strings:
            if palavra.upper() in str(paragrafo_str).upper():
                print('NOTICIA SOBRE:', palavra.upper(), '\n', paragrafo_str, '\n')




















