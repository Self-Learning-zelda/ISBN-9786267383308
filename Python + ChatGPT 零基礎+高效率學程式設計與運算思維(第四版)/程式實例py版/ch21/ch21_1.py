# ch21_1.py
import requests

url = 'http://www.mcut.edu.tw'
htmlfile = requests.get(url)
print(type(htmlfile))


