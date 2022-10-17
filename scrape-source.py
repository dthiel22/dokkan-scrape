from turtle import right
import requests
from bs4 import BeautifulSoup

URL = "https://dbz-dokkanbattle.fandom.com/wiki/Endless_Adventure_Goku_(GT)_%26_Pan_(GT)_%26_Trunks_(GT)?action=edit"
page = requests.get(URL)

# grabbing main part of dokkan page ========
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="wpTextbox1")
print(results.text)
print("==============")
print(results[2])

grabUltra = results.find("")

