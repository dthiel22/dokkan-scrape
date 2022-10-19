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
while x < 100:
    x += 100
    print()
    cardPage = f"https://dbz-dokkanbattle.fandom.com/wiki/All_Cards:_(1){x}_to_(1){x+99}"
    print(cardPage)
    print("=========")
    i = 0
    # iteration needs to be i <= 99 in order to loop through all of it
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
        moveSAName = addLineToTop.replace("|SA name:","\n")
        rEqualSign = moveSAName.replace(" =",":")
        rR1 = rEqualSign.replace("file:Rainbow icon.png|30px|link=Rainbow Ki","Rainbow")
        rA1 = rR1.replace("File:AGL ","")
        rT1 = rA1.replace("File:TEQ ","")
        rI1 = rT1.replace("File:INT ","")
        rS1 = rI1.replace("File:STR ","")
        rP1 = rS1.replace("File:PHY ","")
        rA2 = rP1.replace("File:EAGL ","")
        rT2 = rA2.replace("File:ETEQ ","")
        rI2 = rT2.replace("File:EINT ","")
        rS2 = rI2.replace("File:ESTR ","")
        rP2 = rS2.replace("File:EPHY ","")
        rA3 = rP2.replace("File:SAGL ","")
        rT3 = rA3.replace("File:STEQ ","")
        rI3 = rT3.replace("File:SINT ","")
        rS3 = rI3.replace("File:SSTR ","")
        rP3 = rS3.replace("File:SPHY ","")
        rFile = rS3.replace("File:","")
        rIcon = rFile.replace("icon.png|30px|link=Category:","")
        rQLB = rIcon.replace('"[[',"")
        rQRB = rQLB.replace('"]]',"")
        rLB = rQRB.replace('[[',"")
        rRB = rLB.replace(']]',"")
        rDash = rRB.replace(' - ',", ")
        rBr = rDash.replace('<br>'," ")
        rRef = rBr.replace('<ref>'," ")
        rRef2 = rRef.replace('</ref>',"")
        rRef3 = rRef2.replace('ref ',"")
        rRef4 = rRef3.replace('<>',"+")
        rQuote = rRef4.replace('"',"")
        rName1 = rQuote.replace('name="[1]"',"")
        rName2 = rName1.replace('name="[2]"',"")
        rName3 = rName2.replace('name="[3]"',"")
        rName4 = rName3.replace('name="[4]"',"")
        rName5 = rName4.replace('name="[5]"',"")
        rName6 = rName5.replace('name="[6]"',"")
        rName7 = rName6.replace('name="[7]"',"")
        rName8 = rName7.replace('name="[8]"',"")
        rName9 = rName8.replace('name="[9]"',"")
        rName10 = rName9.replace('name=[10]',"")
        rName11 = rName10.replace('name=[1]',"")
        rName12 = rName11.replace('name=[2]',"")
        rName13 = rName12.replace('name=[3]',"")
        rName14 = rName13.replace('name=[4]',"")
        rName15 = rName14.replace('name=[5]',"")
        rName16 = rName15.replace('name=[6]',"")
        rName17 = rName16.replace('name=[7]',"")
        rName18 = rName17.replace('name=[8]',"")
        rName19 = rName18.replace('name=[9]',"")
        rName20 = rName19.replace('name=[10]',"")
        rSAM = rName20.replace("Super Attack Multipliers|","")
        rKCat = rSAM.replace('Kamehameha (Category)|', "")
        rACat = rKCat.replace('|Androids/Cell Saga', "")


        test = io.StringIO(rACat)
        myline = test.readline()

        # start attribute grabbing from cards
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