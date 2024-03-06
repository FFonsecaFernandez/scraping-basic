from bs4 import BeautifulSoup
import requests

website = 'https://www.bbc.com/mundo/topics/c2lej05epw5t'
result = requests.get(website)
content = result.text


soup = BeautifulSoup(content , 'lxml' )
# soup.find() para una parte especifica
f = open("scraping_html.txt", "w")
f.writelines(soup.prettify())
f.close()
print("scraping finalizado")

