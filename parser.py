import requests
from bs4 import BeautifulSoup as BS



filteredNews = []
allNews = []


r = requests.get("https://monitoringminecraft.ru/novie-servera")
html = BS(r.content, 'html.parser')



allNews = html.findAll(class_='ip_serv')
print(allNews[1].text)
print(allNews[2].text)
print(allNews[3].text)
print(allNews[4].text)
print(allNews[5].text)
print(allNews[6].text)
print(allNews[7].text)
print(allNews[8].text)
print(allNews[9].text)
print(allNews[10].text)
print(allNews[11].text)
print(allNews[12].text)
print(allNews[13].text)
print(allNews[14].text)
print(allNews[15].text)
print(allNews[16].text)
print(allNews[17].text)
print(allNews[18].text)
print(allNews[19].text)
print(allNews[20].text)
print(allNews[21].text)
print(allNews[22].text)
print(allNews[23].text)
print(allNews[24].text)
print(allNews[25].text)
print(allNews[26].text)
print(allNews[27].text)
print(allNews[28].text)
print(allNews[29].text)
print(allNews[30].text)
print(allNews[31].text)
print(allNews[32].text)
print(allNews[33].text)
print(allNews[34].text)
print(allNews[35].text)
print(allNews[36].text)
print(allNews[37].text)
print(allNews[38].text)
print(allNews[39].text)
print(allNews[40].text)
print(allNews[41].text)
print(allNews[42].text)
print(allNews[43].text)
print(allNews[44].text)
print(allNews[45].text)
print(allNews[46].text)
print(allNews[47].text)
print(allNews[48].text)
print(allNews[49].text)








