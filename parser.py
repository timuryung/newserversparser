import requests
from bs4 import BeautifulSoup as BS



filteredNews = []
allNews = []


r = requests.get("https://monitoringminecraft.ru/novie-servera")
html = BS(r.content, 'html.parser')



allNews = html.findAll(class_='ip_serv')
for i in range(0,50):
  print(allNews[i].text)
