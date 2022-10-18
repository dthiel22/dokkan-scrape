from cgitb import text
from operator import contains
from turtle import right
import requests
from bs4 import BeautifulSoup
import io

# test and check io
# msg = "Bob Smith\nJane Doe\nJane,\nPlease order more widgets\nThanks,\nBob\n"
# buf = io.StringIO(msg)
# print(buf.readline())
# print(buf.readline())

# UNIVERSAL VAR

URL = "https://dbz-dokkanbattle.fandom.com/wiki/Planet-Crushing_Blow_Cooler_(Final_Form)?action=edit"
page = requests.get(URL)

# grabbing main part of dokkan page ========
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mw-content-text")
# print(results)

# grabbing text box =====================
print('')
textBoxEl = results.find(id='wpTextbox1').text
addLine = textBoxEl.replace("{{", "----\n{{")
print(addLine)
scanText = addLine
print(scanText)
print("========")

test = io.StringIO(scanText)
readThis = test.readline()

print('--------------')
# causing it to break
# linesLength = int(len(test.readlines()))

# experiment loop
myline = test.readline()
while myline:
    print(myline)
    myline = test.readline()
    if '|name1' in myline:
        print(">>nameone found<<")
        charName1 = myline
    if '|name2' in myline:
        print(">>nametwo found<<")
        charName2 = myline
    if '|Active skill =' in myline:
        print(">>Active Skill found<<")
        charActiveSkill = myline
    if '|rarity =' in myline:
        print(">>rarity found<<")
        charRarity = myline
    if '|type =' in myline:
        print(">>type found<<")
        charType = myline
    if '|ID =' in myline:
        print(">>ID found<<")
        charID = myline
    if '|LS' in myline:
        print(">>LS found<<")
        charLS = myline
    if 'SA type =' in myline:
        print(">>SA type found<<")
        charSaType = myline
    if '|SA description =' in myline:
        print(">>SA type found<<")
        charSaDesc = myline
    if '|UltraSA name =' in myline:
        print(">>SA type found<<")
        charUltra = myline
    if '|UltraSA description =' in myline:
        print(">>SA type found<<")
        charUltraDesc = myline
    if '|PS name =' in myline:
        print(">>SA type found<<")
        charPsName = myline
    if '|PS description =' in myline:
        print(">>SA type found<<")
        charPsDesc = myline
    if '|PS description =' in myline:
        print(">>SA type found<<")
        charPsDesc = myline

print('end loop')
print('')
print(charName1)
print(charName2)
print(charActiveSkill)
print(charRarity)
print(charType)
print(charID)
print(charLS)
print(charSaType)
print(charSaDesc)
print(charUltra)
print(charUltraDesc)
print(charPsName)
print(charPsDesc)
