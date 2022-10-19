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

charName1 = "None"
charName2 = "None"
charRarity = "None"
charType = "None"
charID = "None"
charLS = "None"
charSaType = "None"
charSaDesc = "None"
charUltra = "None"
charUltraDesc = "None"
charPsName = "None"
charPsDesc = "None"
charASName = "None"
charAS = "None"
charASCond = "None"
charTransformType = "None"
charTransformCond = "None"
charLinkkills = "None"
charCategories = "None"

x = 1
while x < 100:
    x += 100
    print()
    cardPage = f"https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1){x}_to_(1){x+99}"
    print(cardPage)
    print("=========")
    i = 0
    # needs to be <= 99 in order to loop through all of it
    while i <= 3:
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
        linkUsed = (f"https://dbz-dokkanbattle.fandom.com{characterSelectEl}?action=edit")
        print(linkUsed)
        
        page = requests.get(linkUsed)

        # grabbing main part of dokkan page ========
        main = BeautifulSoup(page.content, "html.parser")
        content = main.find(id="mw-content-text")
        # print(results)

        # grabbing text box =====================
        print('')
        textBoxEl = content.find(id='wpTextbox1').text
        addLine = textBoxEl.replace("{{", "----\n{{")
        # print(addLine)
        scanText = addLine
        # print(scanText)
        test = io.StringIO(scanText)
        readThis = test.readline()
        print('--------------')

        # start attribute grabbing from cards
        myline = test.readline()
        while myline:
            # print(myline)
            myline = test.readline()
            if '|name1' in myline:
                # print(">>nameone found<<")
                charName1 = myline
            if '|name2' in myline:
                # print(">>nametwo found<<")
                charName2 = myline
            if '|rarity =' in myline:
                # print(">>rarity found<<")
                charRarity = myline
            if '|type =' in myline:
                # print(">>type found<<")
                charType = myline
            if '|ID =' in myline:
                # print(">>ID found<<")
                charID = myline
            if '|LS description =' in myline:
                # print(">>LS found<<")
                charLS = myline
            if '|SA type =' in myline:
                # print(">>SA type found<<")
                charSaType = myline
            if '|SA description =' in myline:
                # print(">>SA description found<<")
                charSaDesc = myline
            if '|UltraSA name =' in myline:
                # print(">>UltraSA found<<")
                charUltra = myline
            if '|UltraSA description =' in myline:
                # print(">>UltraSa Description found<<")
                charUltraDesc = myline
            if '|PS name =' in myline:
                # print(">>PS name found<<")
                charPsName = myline
            if '|PS description =' in myline:
                # print(">>PS descriotion found<<")
                charPsDesc = myline
            if '|Active Skill name =' in myline:
                # print(">>Active Skill name found<<")
                charASName = myline
            if '|Active Skill =' in myline:
                # print(">>Active Skill found<<")
                charAS = myline
            if '|Active Skill condition =' in myline:
                # print(">>Active Skill condition found<<")
                charASCond = myline
            if '|Transform type =' in myline:
                # print(">>Transform type found<<")
                charTransformType = myline
            if '|Transform condition =' in myline:
                # print(">>Transform description found<<")
                charTransformCond = myline
            if '|Link skill =' in myline:
                # print(">>Link skills found<<")
                charLinkSkills = myline
            if '|Category =' in myline:
                # print(">>Link skills found<<")
                charCategories = myline

        print('+++++++++++end attribute check+++++++++++')
        print('')

        
        # assign attributes to CharAttrs object
        c1 = CharAttrs(charName1, charName2, charRarity, charType, charID, charLS, charSaType, charSaDesc, charUltra, charUltraDesc, charPsName, charPsDesc, charASName, charAS, charASCond, charTransformType, charTransformCond, charLinkSkills, charCategories)

        # checks
        print(c1.name1)
        print(c1.name2)
        print(c1.Ultra)
        print('')
        charHolding.append(c1)
        print(charHolding)
        print(charHolding[0].name1)


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