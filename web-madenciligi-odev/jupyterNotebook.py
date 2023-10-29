#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('https://raw.githubusercontent.com/yasinerduran/WebMining/main/products.html')
bs = BeautifulSoup(html.read(), 'html.parser')

table = bs.body.find('table',{'id':'productList'})
productCount = table.findAll('tr')


# In[2]:


urunid = productCount[-1].findAll('td')[0].getText()
print("urunid:"+urunid)
urunAd = productCount[-1].findAll('td')[1].getText()
print("urun adi:"+urunAd)
urunTanim = productCount[-1].findAll('td')[2].getText()
print("urun tanim:"+urunTanim)
urunFiyat = productCount[-1].findAll('td')[3].getText()
print("urun fiyat:"+urunFiyat)


# In[8]:


aranan = input("aramak istediğiniz şey:  ")

metin = bs.get_text()

# Belirli bir kelimeyi arama

if aranan in metin:
    print(aranan+ "kelimesi bulundu." )
else:
    print(aranan+ " kelimesi bulunamadı.")
 
    


# In[ ]:





# In[ ]:




