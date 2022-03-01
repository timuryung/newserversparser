import os
import requests
from bs4 import BeautifulSoup 




welcometext = """   
   Welcome to Minecraft Server parser
   Made by timuryunuk2022
"""

print(welcometext)

print("""Select minecraft monitoring that you want to parse servers from:
1. MonitoringMinecraft
2. TMonitoring
""")



choise = input("Enter you choise (1 or 2): ")





def monitoringminecraft():
  request = requests.get("https://monitoringminecraft.ru/novie-servera")
  content = BeautifulSoup(request.content, 'html.parser')




  ips = content.findAll(class_='ip_serv')
  versions = content.findAll(class_='ver')
  online = content.findAll(itemprop='playersOnline')
  opened = content.findAll(class_='opened')
  try:
    for item in range(0, 50):
      output = ips[item].text + ' ' + 'версия: ' + versions[item].text + ' ' + 'онлайн: ' + online[item].text + ' ' + 'дата открытия: ' + opened[item].text   
      onlineint = int(online[item].text)
      if onlineint > 0:
        print(output)
  except IndexError:
    pass
  #onlineint = int(online.text)

def tmonitoring():
  try:
    for pages in range(1,1000):
      request = requests.get("https://tmonitoring.com/page/" + str(pages))
      content = BeautifulSoup(request.content, 'html.parser')

      ips = content.findAll(class_='ip btn-copy-html')
      name = content.findAll(class_ = 'name pull-left')

    try:
      for item in range(0,37898):
        output = ips[item].text + ' '  + name[item].text
        print(output)
    except IndexError:
      pass


  except IndexError:
    pass


if choise == '1':
  monitoringminecraft()
elif choise == '2':
  tmonitoring()
else:
  print("Wrong input! Try again!")
  os.system('python3 parser.py')




