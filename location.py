import requests
import pandas as pd
from bs4 import BeautifulSoup

def getdata(url):
	r=requests.get(url)
	return r.text
api = 'b59a16f198e0a7f534f16ed78abfc87d'
number = '9831003926'
country = 'IN'
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)