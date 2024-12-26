import requests
from bs4 import BeautifulSoup
url = "https://www.flipkart.com/"
r = requests.get(url)



soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all("h6"):
  print(heading.text)
