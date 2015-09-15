import requests
from bs4 import BeautifulSoup

def spider(max_pages):
	page=1
	while page <= max_pages :
		url= 'https://www.thenewboston.com/forum/recent_activity.php?page='+ str(page)
		source_code=requests.get(url)
		plain_text=source_code.text
		soup=BeautifulSoup(plain_text)
		for link in soup.findAll('a',{'class':'post-title'}):
			href='https://www.thenewboston.com'+link.get('href')
			title=link.string
			print(title + " :\n")
			print(href  + "\n")
		page+=1

spider(1)
