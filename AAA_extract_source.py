from cgitb import text
from dataclasses import replace
from operator import contains
from turtle import right
import requests
from bs4 import BeautifulSoup
import io

# UNIVERSAL VAR
extraSpace1 = '{\n'
charName1 = "|None \n"
charName2 = "|None \n"
charRarity = "|None \n"
charType = "|None \n"
charID = "|None \n"
charLS = "|None \n"
charSaType = "|None \n"
charSaDesc = "|None \n"
charUltra = "|None \n"
charUltraDesc = "|None \n"
charPsName = "|None \n"
charPsDesc = "|None \n"
charASName = "|None \n"
charAS = "|None \n"
charASCond = "|None \n"
charTransformType = "|None \n"
charTransformCond = "|None \n"
charLinkSkills = "|None \n"
charCategories = "|None \n"
extraSpace2 = '},\n'

# loops through pages of cards x < 2600 ========
x = 1
while x < 2600:
    x += 100
    print()
    cardPage = f"https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1){x}_to_(1){x+99}"
    print(cardPage)
    print("=========")
    i = 0
    # iteration needs to be i <= 99 in order to loop through all of it
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
        linkUsed = (f"https://dbz-dokkanbattle.fandom.com{characterSelectEl}?action=edit")
        print(linkUsed)
        print("main card page ======================")
        page = requests.get(linkUsed)

        # grabbing main part of dokkan page + text box ========
        main = BeautifulSoup(page.content, "html.parser")
        content = main.find(id="mw-content-text")
        textBoxEl = content.find(id='wpTextbox1').text
        # print(results)

        # adding top line for formatting (doesn't cut character name when iterating later) and = => + for formating =====================
        print('')
        addLineToTop = textBoxEl.replace("{{", "----\n{{")
        replaceEqualSign = addLineToTop.replace(" =",":")
        rR = replaceEqualSign.replace("[[file:Rainbow icon.png|30px|link=Rainbow Ki","")
        rA = rR.replace("[[file:AGL icon.png|30px|link=Category: AGL","")
        rT = rA.replace("[[File:TEQ icon.png|30px|link=Category: TEQ","")
        rI = rT.replace("[[file:INT icon.png|30px|link=Category: INT","")
        rS = rI.replace("[[file:STR icon.png|30px|link=Category: STR","")
        rP = rS.replace("[[file:PHY icon.png|30px|link=Category: PHY","")
        rSAM = rP.replace("[[Super Attack Multipliers|","")
        rQLB = rSAM.replace('"[[',"")
        rQRB = rQLB.replace('"]]',"")
        rLB = rQRB.replace('[[',"")
        rRB = rLB.replace(']]',"")
        rDash = rRB.replace(' - ',"\n")
        rBr = rDash.replace('<br>'," ")
        rRef = rBr.replace('<ref>'," ")
        rRef2 = rRef.replace('</ref>',"")
        rName = rRef2.replace('name="[1]"',"")


        test = io.StringIO(rName)
        # readThis = test.readline()

        # start attribute grabbing from cards
        myline = test.readline()
        while myline:
            # print(myline)
            myline = test.readline()
            if '|name1:' in myline:
                # print(">>nameone found<<")
                charName1 = myline
            if '|name2:' in myline:
                # print(">>nametwo found<<")
                charName2 = myline
            if '|rarity:' in myline:
                # print(">>rarity found<<")
                charRarity = myline
            if '|type:' in myline:
                # print(">>type found<<")
                charType = myline
            if '|ID:' in myline:
                # print(">>ID found<<")
                charID = myline
            if '|LS description:' in myline:
                # print(">>LS found<<")
                charLS = myline
            if '|SA type:' in myline:
                # print(">>SA type found<<")
                charSaType = myline
            if '|SA description:' in myline:
                # print(">>SA description found<<")
                charSaDesc = myline
            if '|UltraSA name:' in myline:
                # print(">>UltraSA found<<")
                charUltra = myline
            if '|UltraSA description:' in myline:
                # print(">>UltraSa Description found<<")
                charUltraDesc = myline
            if '|PS name:' in myline:
                # print(">>PS name found<<")
                charPsName = myline
            if '|PS description:' in myline:
                # print(">>PS descriotion found<<")
                charPsDesc = myline
            if '|Active Skill name:' in myline:
                # print(">>Active Skill name found<<")
                charASName = myline
            if '|Active Skill:' in myline:
                # print(">>Active Skill found<<")
                charAS = myline
            if '|Active Skill condition:' in myline:
                # print(">>Active Skill condition found<<")
                charASCond = myline
            if '|Transform type:' in myline:
                # print(">>Transform type found<<")
                charTransformType = myline
            if '|Transform condition:' in myline:
                # print(">>Transform description found<<")
                charTransformCond = myline
            if '|Link skill:' in myline:
                # print(">>Link skills found<<")
                charLinkSkills = myline
            if '|Category:' in myline:
                # print(">>Link skills found<<")
                charCategories = myline
        print('+++++++++++end attribute check+++++++++++')
        print('')

        results = [extraSpace1, charName1, charName2, charRarity, charType, charID, charLS, charSaType, charSaDesc, charUltra, charUltraDesc, charPsName, charPsDesc, charASName, charAS, charASCond, charTransformType, charTransformCond, charLinkSkills, charCategories, extraSpace2]

        with open('out.txt', 'a', encoding='utf-8') as output:
            output.writelines(results)