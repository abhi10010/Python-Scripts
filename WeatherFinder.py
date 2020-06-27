import requests
from bs4 import BeautifulSoup

def weatherSearch(cityName):
  
  search = 'weather in ' + cityName
  url = f"https://www.google.com/search?&q={search}"
  req = requests.get(url)
  
  soup = BeautifulSoup(req.text, "html.parser")
  temp_f = soup.find("div", class_ = "BNeawe").text
  
  temp_f_split = temp_f.split('°')
  temp_c = int((int(temp_f_split[0]) - 32) * (5/9))
  print('{}°C or {}'.format(temp_c, temp_f))
  
weatherSearch('Toronto')
