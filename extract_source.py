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
charHolding = []
class CharAttrs:
    def __init__(self, name1, name2, rarity, cType, ID, LS, SaType, SaDesc, Ultra, UltraDesc, PSName, PSDesc, ASName, AS, ASCond, TransformType, TransformCond, Links, Categories):
        self.name1 = name1
        self.name2 = name2
        self.rarity = rarity
        self.cType = cType
        self.ID = ID
        self.LS = LS
        self.SaType = SaType
        self.SaDesc = SaDesc
        self.Ultra = Ultra
        self.UltraDesc = UltraDesc
        self.PSName = PSName
        self.PSDesc = PSDesc
        self.ASName = ASName
        self.AS = AS
        self.ASCond = ASCond
        self.TransformType = TransformType
        self.TransformCond = TransformCond
        self.Links = Links
        self.Categories = Categories

charName1 = ""
charName2 = ""
charRarity = ""
charType = ""
charID = ""
charLS = ""
charSaType = ""
charSaDesc = ""
charUltra = ""
charUltraDesc = ""
charPsName = ""
charPsDesc = ""
charActiveSkillName = ""
charActiveSkill = ""
charActiveSkillCond = ""
charTransformType = ""
charTransformCond = ""
charLinkSkills = ""
charCategories = ""

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
    if '|rarity =' in myline:
        print(">>rarity found<<")
        charRarity = myline
    if '|type =' in myline:
        print(">>type found<<")
        charType = myline
    if '|ID =' in myline:
        print(">>ID found<<")
        charID = myline
    if '|LS description =' in myline:
        print(">>LS found<<")
        charLS = myline
    if '|SA type =' in myline:
        print(">>SA type found<<")
        charSaType = myline
    if '|SA description =' in myline:
        print(">>SA description found<<")
        charSaDesc = myline
    if '|UltraSA name =' in myline:
        print(">>UltraSA found<<")
        charUltra = myline
    if '|UltraSA description =' in myline:
        print(">>UltraSa Description found<<")
        charUltraDesc = myline
    if '|PS name =' in myline:
        print(">>PS name found<<")
        charPsName = myline
    if '|PS description =' in myline:
        print(">>PS descriotion found<<")
        charPsDesc = myline
    if '|Active skill name =' in myline:
        print(">>Active skill name found<<")
        charActiveSkillName = myline
    if '|Active skill =' in myline:
        print(">>Active skill found<<")
        charActiveSkill = myline
    if '|Active skill condition =' in myline:
        print(">>Active skill condition found<<")
        charActiveSkillCond = myline
    if '|Transform type =' in myline:
        print(">>Transform type found<<")
        charTransformType = myline
    if '|Transform condition =' in myline:
        print(">>Transform description found<<")
        charTransformCond = myline
    if '|Link skill =' in myline:
        print(">>Link skills found<<")
        charLinkSkills = myline
    if '|Category =' in myline:
        print(">>Link skills found<<")
        charCategories = myline


print('+++++++++++end loop+++++++++++')
print('')

c1 = CharAttrs(charName1, charName2, charRarity, charType, charID, charLS, charSaType, charSaDesc, charUltra, charUltraDesc, charPsName, charPsDesc, charActiveSkillName, charActiveSkill, charActiveSkillCond, charTransformType, charTransformCond, charLinkSkills, charCategories)


# if charName1 == "":
#     print('no name found')
# print(charName2)
# print(charRarity)
# print(charType)
# print(charID)
# print(charLS)
# print(charSaType)
# print(charSaDesc)
# print(charUltra)
# print(charUltraDesc)
# print(charPsName)
# print(charPsDesc)
# if charActiveSkillName == "":
#     print('no active skill found')
# print(charActiveSkillName)
# print(charActiveSkill)
# print(charActiveSkillCond)
# print(charTransformType)
# print(charTransformCond)
# print(charLinkSkills)
# print(charCategories)