import sys
from bs4 import BeautifulSoup
import requests
import re

url = sys.argv[1]

def makeurls(url):
	soup = []
	source = requests.get(url)
	soup = source.text
	soup = BeautifulSoup((soup), "lxml")
	soup = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", str(soup), flags=re.MULTILINE)
	soup = list(dict.fromkeys(soup))
	return(soup)


for email in makeurls(url):
	print(email)

