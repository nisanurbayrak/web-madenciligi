#!/usr/bin/env python
# coding: utf-8

# In[6]:


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.sikayetvar.com/apple-store'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

req = Request(url, headers=headers)
html = urlopen(req)
bs = BeautifulSoup(html.read(), 'html.parser')


# In[116]:


tarihler = bs.body.find_all('div', {'class': 'profile-desc'})[:10]
yorumlar = bs.body.find_all('p', {'class': 'complaint-description'})[:10]
 
for yorum in yorumlar:
    for tarih in tarihler:
       print(tarih.get_text()+"\n"+yorum.get_text(strip=True)+"\n"+(("-")*50))


# In[ ]:




