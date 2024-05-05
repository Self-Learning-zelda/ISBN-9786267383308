# ch21_6.py
import requests

url = 'https://www.kingstone.com.tw/' 
htmlfile = requests.get(url)
htmlfile.raise_for_status()

