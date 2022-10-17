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

# grabbing the character ID
characterIdEl = characterIdTableEl.select("center")[12].text
# print(characterIdEl)
# print("=====")

# grabbing right column
rightTableEl = results.find(class_="righttablecard")
print(rightTableEl)
print("========")

# NEXT TO DO......GRAB CERTAIN tds OFF OF PAGE....PLAN IS TO MAKE LOOP IF 5,6,7,8 sections are there...then....

grabTd = rightTableEl.select('td', attrs={'colspan': '2'})[1]
print(grabTd.text)

# # THIS IS FOR GRABBING ALL INDIVIDUAL SLOTS
# # grabbing leader skill
# leaderSkillEl = rightTableEl.select("td")[1].text
# print(leaderSkillEl)
# print("======")
# # grabbing super attack
# superAttackEl = rightTableEl.select("td")[4].text
# print(superAttackEl)
# print('=======')
# # grabbing ultra super attack
# ultraSuperAttackEl = rightTableEl.select("td")[7].text
# print(ultraSuperAttackEl)
# print('========')
# # grabbing passive skill
# passiveSkillEl = rightTableEl.select("td")[10].text
# print(passiveSkillEl)
# print('=========')
# # grabbing active skill
# activeSkillEl = rightTableEl.select("td")[13].text
# print(activeSkillEl)
# print('=======')
# # grabbing activation
# activationConditionEl = rightTableEl.select("td")[15].text
# print(activationConditionEl)
# print('=======')
# # grabbing link skills
# linkSkillsEl = rightTableEl.select("td")[17].text
# print(linkSkillsEl)
# print('=======')
# # grabbing categories
# categoriesEL = rightTableEl.select("td")[19]
# print(categoriesEL.text)
# print('=======')