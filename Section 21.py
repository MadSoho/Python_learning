import requests
from bs4 import BeautifulSoup

source=requests.get("http://pythonhow.com/example.html").content
soup=BeautifulSoup(source,"html.parser")
extract=soup.find_all("div",{"class":"cities"})

for city in extract:
    print(city.find_all("h2")[0].text)
