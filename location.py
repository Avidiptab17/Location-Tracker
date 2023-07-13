import requests
import pandas as pd
from bs4 import BeautifulSoup

def getdata(url):
	r=requests.get(url)
	return r.text
api = 'Your API Key'
number = 'Phone Number'
country = 'Country Code'
htmldata=getdata('http://apilayer.net/api/validate?access_key='+api+'&number='+number+'&country_code='+country+'&format=1')
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup)
