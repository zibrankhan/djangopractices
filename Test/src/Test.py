import requests
from bs4 import BeautifulSoup

r = requests.get("https://stackoverflow.com/questions/45047093/using-python-faker-library-but-have-import-error")
print(r.content)
soup = BeautifulSoup(r.content, 'html.parser')
#link = soup.find_all('a')
#for i in link:
    #print(i.get('href'))
    
div = soup.find_all('div',attrs={'class':'post-text','itemprop':'text'})

print(div[0].text)
#print(div[1].text)

ans = soup.find_all('div',attrs={'class':'answercell post-layout--right'})
for i in ans:
    print("----"*40)
    print(str(i.text).replace("\n"," "))