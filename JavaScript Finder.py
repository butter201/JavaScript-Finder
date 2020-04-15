import requests
from bs4 import BeautifulSoup
url=input("BULMAK ISTEDIGINIZ SAYFANIN URLSINI GIRINIZ ==>")
response=requests.get(url)
icerik=response.content
soup=BeautifulSoup(icerik,"html.parser")
script=soup.find_all("script")
for i in script:
    print(i)
    print("-------")