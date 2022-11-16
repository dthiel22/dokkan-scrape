# Import required modules
from lxml import html
import requests

# Request the page
page = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

# Parsing the page
tree = html.fromstring(page.content)

# Get element using XPath
prices = tree.xpath(
    '//div[@class="col-sm-4 col-lg-4 col-md-4"]/div/div[1]/h4[1]/text()')
print(prices)

# ==============================
# from bs4 import BeautifulSoup
# import io
# import requests

# # COPY HERE FOR SCRAPE ALL
# URL2 = (f"https://dbz-dokkanbattle.fandom.com/wiki/All_Link_Skills?action=edit")
# print(URL2)

# print(
#     "=============================== main category page ===============================")
# # grabbing main part of dokkan page + text box ========
# linkUsed = requests.get(URL2)
# main = BeautifulSoup(linkUsed.content, "html.parser")
# content = main.find(id="mw-content-text")
# textBoxEl = content.find(id='wpTextbox1').text

# # check before global edits =============
# print('')

# # ======= this is POST-EDITING print =======
# # print(rRB)
# test = io.StringIO(textBoxEl)

# # start attribute editing from cards ==================
# stringedScrape = textBoxEl.replace(
#     '}}  ', '').replace('}} ', '').replace('}}', '').replace(' style="width:220px"|', '')

# with open('category-list.txt', 'w', encoding="utf-8") as output:
#     output.writelines(stringedScrape)

# readFile = open("category-list.txt").readlines()
# allLinks = []
# parsing = False
# for line in readFile:
#     if line.startswith("#"):
#         parsing = True
#     if line.startswith("!{"):
#         parsing = True
#     if line.startswith("|") or line.endswith('JP') or line.endswith('|JP') or line.endswith('JP\n'):
#         parsing = False
#         # print('line not needed')
#     if parsing:
#         print(line)
#         allLinks.append(line.replace(
#             '|', '').replace('!{{Categories', '').replace(')', '').replace('JP', ''))
# seen = set()
# finalLinks = []
# for oneLink in allLinks:
#     if oneLink not in seen:
#         seen.add(oneLink)
#         finalLinks.append(oneLink)

# with open('ALL-CATS.txt', 'w', encoding="utf-8") as linkFile:
#     linkFile.writelines(finalLinks)

# //*[@id = "mw-content-text"]/div[1]/div/div[2]/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[1]/td[2]
