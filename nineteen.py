# Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

# The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

from bs4 import BeautifulSoup
import requests

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

a = soup.select("p")

for i in a:
    print(i.text)
