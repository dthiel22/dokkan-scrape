# Import required modules
from lxml import html
from bs4 import BeautifulSoup
import requests

# Request the page
page = requests.get('https://dbz-dokkanbattle.fandom.com/wiki/All_Link_Skills')

# Parsing the page
tree = html.fromstring(page.content)

# tree.xpath('//*[@id="mw-content-text"]/div[1]/div/div[2]/table[2]/tbody/tr[267]/td[2]/table/tbody/tr[2]/td[2]')

i=3
soup = BeautifulSoup(page.content, "html.parser")
contentsOfPage = soup.find(id="content")
# selecting the character URLs ============
linkListTable = contentsOfPage.findAll("table")
# print(linkListTable[1])
linkTotaltrs = linkListTable[1].findAll("tbody")
numOftrs = len(linkTotaltrs)
print(numOftrs)

linkArr =[]
while i <= numOftrs :
    linkName = tree.xpath(f'//*[@id="mw-content-text"]/div[1]/div/div[2]/table[2]/tbody/tr[{i}]/td[1]/a/text()')
    print('=============')
    print('link name')
    print(linkName[0])
    print('=============')
    linkLvl1 = tree.xpath(f'//*[@id="mw-content-text"]/div[1]/div/div[2]/table[2]/tbody/tr[{i}]/td[2]/table/tbody/tr[1]/td[2]/text()')
    print('link lvl 1')
    print(linkLvl1[0])
    print('=============')
    linkLvl10 = tree.xpath(f'//*[@id="mw-content-text"]/div[1]/div/div[2]/table[2]/tbody/tr[{i}]/td[2]/table/tbody/tr[2]/td[2]/text()')
    print('link lvl 10')
    print(linkLvl10[0])
    print('+++++++++++++++')
    i+=2

    linkArr.append('{\n')
    linkArr.append('name:'+'"'+linkName[0]+'",'+'\n')
    linkArr.append('lvl1_stats:'+'"'+linkLvl1[0]+'",'+'\n')
    linkArr.append('lvl10_stats:'+'"'+linkLvl10[0]+'",'+'\n')
    linkArr.append('},\n')

    with open('link-table.js', 'w', encoding="utf-8") as linkFile:
        linkFile.writelines(linkArr)