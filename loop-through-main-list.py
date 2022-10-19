from turtle import right
import requests
from bs4 import BeautifulSoup

# # getting URL stuff ===========
# URL = "https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1)001_to_(1)100"
# page = requests.get(URL)

# # grabbing main part of dokkan page ========
# soup = BeautifulSoup(page.content, "html.parser")
# results = soup.find(id="content")
# # print(results.prettify())

# # grabbing top table ===========
# characterListIdEl = results.find("table")
# # print(characterListIdEl.prettify())

# loops through pages of cards x < 2600 ========
x = 1
while x < 200:
    x += 100
    print()
    cardPage = f"https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1){x}_to_(1){x+99}"
    print(cardPage)
    print("=========")
    i = 0
    # needs to be <= 99 in order to loop through all of it
    while i <= 5:
        i += 1
        URL = cardPage
        page = requests.get(URL)

        # grabbing main part of dokkan page ========
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find(id="content")

        # selecting the character links ============
        characterListIdEl = results.find("table")
        characterTdEl = characterListIdEl.select("tr")[i]
        characterSelectEl = (characterTdEl).select("a")[1]["href"]
        linkUsed = (f"https://dbz-dokkanbattle.fandom.com{characterSelectEl}")
        print(linkUsed)
        


# loop through page selecting character links ===========
# i = 0
# while i <= 99:
#     i += 1
#     characterTdEl = characterListIdEl.select("tr")[i]
#     characterSelectEl = (characterTdEl).select("a")[1]["href"]
#     linkUsed = (f"https://dbz-dokkanbattle.fandom.com{characterSelectEl}")
#     print(linkUsed)
