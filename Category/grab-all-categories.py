from bs4 import BeautifulSoup
import io
import requests

# COPY HERE FOR SCRAPE ALL
URL2 = (f"https://dbz-dokkanbattle.fandom.com/wiki/All_Character_Categories?action=edit")
print(URL2)

print(
    "=============================== main category page ===============================")
# grabbing main part of dokkan page + text box ========
linkUsed = requests.get(URL2)
main = BeautifulSoup(linkUsed.content, "html.parser")
content = main.find(id="mw-content-text")
textBoxEl = content.find(id='wpTextbox1').text

# check before global edits =============
print('')

# ======= this is POST-EDITING print =======
# print(rRB)
test = io.StringIO(textBoxEl)

# start attribute editing from cards ==================
stringedScrape = textBoxEl.replace(
    '}}  ', '').replace('}} ', '').replace('}}', '').replace(' style="width:220px"|', '')

with open('/Users/alexthiel/code/dokkan-scrape/Category/category-list.txt', 'w', encoding="utf-8") as output:
    output.writelines(stringedScrape)

readFile = open(
    "/Users/alexthiel/code/dokkan-scrape/Category/category-list.txt").readlines()
allCategories = []
parsing = False
for line in readFile:
    if line.startswith("#"):
        parsing = True
    if line.startswith("!{"):
        parsing = True
    if line.startswith("|") or line.endswith('JP') or line.endswith('|JP') or line.endswith('JP\n'):
        parsing = False
        # print('line not needed')
    if parsing:
        print(line)
        allCategories.append(line.replace(
            '|', '').replace('!{{Categories', '').replace(')', '').replace('JP', ''))

seen = set()
finalCategories = []
categoryID = 0
for oneChar in allCategories:
    if oneChar not in seen:
        categoryID += 1
        stringCatID = str(categoryID)
        seen.add(oneChar)
        finalCategories.append('{\n')
        finalCategories.append('id: '+stringCatID+'\n')
        finalCategories.append('name: '+'"'+oneChar.replace('\n', '')+'"')
        finalCategories.append('\n},\n')


with open('/Users/alexthiel/code/dokkan-scrape/Category/API-category.js', 'w', encoding="utf-8") as categoryFile:
    categoryFile.writelines(finalCategories)
