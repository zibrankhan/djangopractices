import requests
from bs4 import BeautifulSoup

r = requests.get("https://stackoverflowhttps://stackoverflow.com/questions/46902357/error-loading-mysqldb-module-did-you-install-mysqlclient-or-mysql-python.com/questions/45047093/using-python-faker-library-but-have-import-error")
soup = BeautifulSoup(r.content, 'html.parser')
div = soup.find_all('div',attrs={'class':'inner-content clearfix'})

print(div[0].text)