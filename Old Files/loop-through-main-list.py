import requests
from bs4 import BeautifulSoup


# loops through pages of cards x < 2600 ========
x = 1
while x < 800:
    x += 100
    print()
    cardPage = f"https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1){x}_to_(1){x+99}"
    print(cardPage)
    print("=========")
    # grabbing main part of dokkan page ========
    URL = cardPage
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="content")
    # selecting the character links ============
    characterListIdEl = results.find("table")
    characterTbody = results.findAll("tr")
    numOfCharacters = len(characterTbody)
    print(numOfCharacters)
    i = 0
    # needs to be <= 99 in order to loop through all of it
    while i <= numOfCharacters-2:
        i += 1
        characterTdEl = characterListIdEl.select("tr")[i]
        characterSelectEl = (characterTdEl).select("a")[1]["href"]
        linkUsed = (f"https://dbz-dokkanbattle.fandom.com{characterSelectEl}")
        print(linkUsed)
