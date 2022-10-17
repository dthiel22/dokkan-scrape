from operator import contains
from turtle import right
import requests
from bs4 import BeautifulSoup

URL = "https://dbz-dokkanbattle.fandom.com/wiki/Planet-Crushing_Blow_Cooler_(Final_Form)"
page = requests.get(URL)

# grabbing main part of dokkan page ========
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mw-content-text")

# grabbing top table with Max lvl, SA lvl, rarity, type,cost,ID ===========
characterIdTableEl = results.find("table")

# grabbing the character ID ==================
characterIdEl = characterIdTableEl.select("center")[12].text
print()
print('Character ID: ' + characterIdEl)
# print("=====")

# grabbing right column =====================
rightTableEl = results.find(class_="righttablecard")
# print(rightTableEl)
# print("========")

# grabbing right stats ========
rightStats = rightTableEl.find('table')

# grab all img on right side column
allImgEl = rightStats.find_all('img')

# loop to find attributes of card==================================
i = 0
ultraSuperT = False
activeSkillT = False
while i < len(allImgEl):
    selectAttr = str(allImgEl[i].attrs)
    print(selectAttr)
    if 'Ultra' in selectAttr:
        ultraSuperT = True
        print('yes Ultra Super')

    if 'Active' in selectAttr:
        activeSkillT = True
        print('yes Active Skill')

    i += 1
    print('=====')

if ultraSuperT == True and activeSkillT == True:
    print(">>>Ultra Super and Active Skill<<<")
    print("-----------")
    # THIS IS FOR GRABBING ALL INDIVIDUAL SLOTS
    # grabbing leader skill
    leaderSkillEl = rightTableEl.select("td")[1].text
    print(leaderSkillEl)
    print("======")
    # grabbing super attack
    superAttackEl = rightTableEl.select("td")[4].text
    print(superAttackEl)
    print('=======')
    # grabbing ultra super attack
    ultraSuperAttackEl = rightTableEl.select("td")[7].text
    print(ultraSuperAttackEl)
    print('========')
    # grabbing passive skill
    passiveSkillEl = rightTableEl.select("td")[10].text
    print(passiveSkillEl)
    print('=========')
    # grabbing active skill
    activeSkillEl = rightTableEl.select("strong")[3].text
    print(activeSkillEl)
    print('=======')
    # grabbing activation
    activationConditionEl = rightTableEl.select("td")[14].text
    print(activationConditionEl)
    print('=======')
    # grabbing link skills
    linkSkillsEl = rightTableEl.select("td")[16].text
    print(linkSkillsEl)
    print('=======')
    # grabbing categories
    categoriesEL = rightTableEl.select("td")[18].text
    print(categoriesEL)
    print('=======')

if ultraSuperT == True and activeSkillT == False:
    print(">>>Ultra Super<<<")
    print("-----------")
    leaderSkillEl = rightTableEl.select("td")[1].text
    print(leaderSkillEl)
    print("======")
    # grabbing super attack
    superAttackEl = rightTableEl.select("td")[4].text
    print(superAttackEl)
    print('=======')
    # grabbing ultra super attack
    ultraSuperAttackEl = rightTableEl.select("td")[7].text
    print(ultraSuperAttackEl)
    print('========')
    # grabbing passive skill
    passiveSkillEl = rightTableEl.select("td")[10].text
    print(passiveSkillEl)
    print('=========')
    # grabbing link skills
    linkSkillsEl = rightTableEl.select("td")[12].text
    print(linkSkillsEl)
    print('=======')
    # grabbing categories
    categoriesEL = rightTableEl.select("td")[14].text
    print(categoriesEL)
    print('=======')
if ultraSuperT == False and activeSkillT == True:
    print(">>>Active Skill<<<")
    print("-----------")
    leaderSkillEl = rightTableEl.select("td")[1].text
    print(leaderSkillEl)
    print("======")
    # grabbing super attack
    superAttackEl = rightTableEl.select("td")[4].text
    print(superAttackEl)
    print('=======')
    # grabbing passive skill
    passiveSkillEl = rightTableEl.select("td")[7].text
    print(passiveSkillEl)
    print('=========')
    # grabbing active skill
    activeSkillEl = rightTableEl.select("strong")[2].text
    print(activeSkillEl)
    print('=======')
    # grabbing activation
    activationConditionEl = rightTableEl.select("td")[11].text
    print(activationConditionEl)
    print('=======')
    # grabbing link skills
    linkSkillsEl = rightTableEl.select("td")[13].text
    print(linkSkillsEl)
    print('=======')
    # grabbing categories
    categoriesEL = rightTableEl.select("td")[15].text
    print(categoriesEL)
    print('=======')
if ultraSuperT == False and activeSkillT == False:
    print('>>>NO Ultra Super or Active Skill<<<')
    print("-----------")
    leaderSkillEl = rightTableEl.select("td")[1].text
    print(leaderSkillEl)
    print("======")
    # grabbing super attack
    superAttackEl = rightTableEl.select("td")[4].text
    print(superAttackEl)
    print('=======')
    # grabbing passive skill
    passiveSkillEl = rightTableEl.select("td")[7].text
    print(passiveSkillEl)
    print('=========')
    # grabbing link skills
    linkSkillsEl = rightTableEl.select("td")[9].text
    print(linkSkillsEl)
    print('=======')
    # grabbing categories
    categoriesEL = rightTableEl.select("td")[11].text
    print(categoriesEL)
    print('=======')
print('====end of code====')
