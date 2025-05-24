import requests as r
from bs4 import BeautifulSoup as bs

try:
    resultado = r.get('https://www.uol.com.br')
    resultado2 = r.get('https://www.gov.br/pt-br')
    resultado3 = r.get('https://explozaogamer.com.br/#google_vignette')
except Exception as erro:
    print('Erro: ', erro)

else:
    resposta = resultado.text
    soup = bs(resposta, 'html.parser')
    resposta2 = resultado2.text
    soup2 = bs(resposta2, 'html.parser')
    resposta3 = resultado3.text
    soup3 = bs(resposta3, 'html.parser')
    print (soup.find("html").prettify())
    print (soup2.title.string)
    print (soup3.title.string)

















































