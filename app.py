import requests
from bs4 import BeautifulSoup
def web(page,WebUrl):
    if(page>0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        for link in s.findAll('a', {'class':'s-access-detail-page'}):
            tet = link.get('title')
            print(tet)
            tet_2 = link.get('href')
            print(tet_2)
web(1,'https://www.amazon.in/s/ref=mega_elec_s23_1_1_1_1?rh=i%3Aelectronics%2Cn%3A1389401031&ie=UTF8&bbn=976419031')
