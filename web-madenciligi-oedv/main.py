from urllib.request import urlopen
from bs4 import BeautifulSoup

def main():
    url =  "C:\Users\Nisa\Desktop\web-madenciligi-oedv\index.html"
    html = urlopen(url)
    bs4 = BeautifulSoup(html.read(), 'html.parser')

    div_list = bs4.findAll('div')
    for div_list in div_list:
        print(div_list.get_text())

if name == 'main':
    main()
