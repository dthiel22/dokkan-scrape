from bs4 import BeautifulSoup
import io
import os
import requests


URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Fusion_with_the_Big_Gete_Star_Metal_Cooler?action=edit")
print(URL2)

print("main card page ======================")
# grabbing main part of dokkan page + text box ========
linkUsed = requests.get(URL2)
main = BeautifulSoup(linkUsed.content, "html.parser")
content = main.find(id="mw-content-text")
textBoxEl = content.find(id='wpTextbox1').text
        
# global edits to text =====================
print('')
rQuote = textBoxEl.replace('"',"")
# check before global edits =============
# print(rQuote)

# specified/prepping content ============
rSAType = rQuote.replace('|SA type = Ki',"").replace('|SA type =  Ki',"").replace('|SA Type = Ki',"").replace('|SA type = M',"").replace('|SA type = W',"").replace('|SA type =',"").replace('|UltraSA type = Ki',"").replace('|UltraSA type =  K:',"").replace('|UltraSA type = M',"").replace('|UltraSA type = W',"").replace('|UltraSA type =',"").replace('|SA type Active = Ki',"").replace('|SA type Active = M',"").replace('|SA type Active = W',"").replace('|SA type Active =',"")
rPettan = rSAType.replace('|Pettan = yes',"")
rMoveASCond = rPettan.replace('|Active skill condition','\n|Active skill condition')
rTube = rMoveASCond.replace('|','"')
rEqualSign = rTube.replace(" =",'":')
rLineBreak = rEqualSign.replace('<br>',"").replace('</br>',"")

# prints all pre-edit material...GREAT for finding what needs to be edited for specific cases ============
# print(rLineBreak)

# further content prunning ================
rServerIcon = rLineBreak.replace('File:Japan server.png"20px',"").replace('File:Global server.png"20px',"")

rExtraCatInLink = rServerIcon.replace('Androids-Cell Saga"',"").replace('Kamehameha (Category)"',"").replace('Otherworld Warriors (Link Skill)"',"").replace('Turtle School (Link Skill)"',"").replace('Namekians (Link Skill)"',"").replace('Team Bardock (Link Skill)"',"").replace(':Category:Extreme Class"',"").replace(':Category:Super Class"',"").replace('Fusion (Link Skill)"',"")

rExtraDisambig = rExtraCatInLink.replace('Goku (disambiguation)"',"").replace('Goku (disambiguation)#Goku"',"").replace('Goku (disambiguation)#Goku (Angel)"',"").replace('Goku (disambiguation)#Goku (Youth)"',"").replace('Caulifla (disambiguation)"',"").replace('Cooler (disambiguation)"',"").replace('Trunks (disambiguation)"',"").replace('Bardock (disambiguation)"',"").replace('Android 18 (disambiguation)#Android #18"',"").replace('(disambiguation)#Ribrianne"',"").replace('Rozie (disambiguation)"',"").replace('Kakunsa (disambiguation)"',"").replace('Kale (disambiguation)"',"").replace('Tapion (disambiguation)"',"").replace('Gohan (disambiguation)#Gohan (Kid)"',"").replace('Frieza (disambiguation)"',"").replace('Vegeta (disambiguation)"',"").replace('Cooler (disambiguation)#Metal Cooler"',"").replace('Giru (disambiguation)"',"").replace('Cell (disambiguation)"',"").replace('Boujack (disambiguation)"',"").replace('Gohan (disambiguation)#Gohan (Teen)"',"").replace('Gohan (disambiguation)#Ultimate Gohan"',"").replace('Gohan (disambiguation)#Great Saiyaman"',"").replace('Trunks (disambiguation)#Trunks (Kid)"',"").replace('Trunks (disambiguation)#Trunks (Teen)"',"").replace('Goten (disambiguation)#Goten (Kid)"',"").replace('Piccolo (disambiguation)#Piccolo"',"").replace('Cell (disambiguation)#Cell (Perfect Form)"',"").replace('Cell (disambiguation)#Perfect Cell"',"").replace('Gohan (disambiguation)#Super Saiyan Gohan (Youth)"',"").replace('Gohan (disambiguation)#Super Saiyan 2 Gohan (Youth)"',"").replace('Android 14 (disambiguation)#Androids #14 & #15"',"").replace('Android 16 (disambiguation)"',"").replace('Android 17 (disambiguation)#Android #17"',"").replace('Android 18 (disambiguation)#Android #18 (Future)"',"").replace('Android 17 (disambiguation)#Android #17 (Future)"',"").replace('Ginyu (disambiguation)"',"").replace('Android 13 (disambiguation)#Android #13"',"").replace('Android 13 (disambiguation)#Fusion Android #13"',"").replace('Zamasu (disambiguation)#Zamasu"',"").replace('Zamasu (disambiguation)#Goku Black"',"").replace('Trunks (disambiguation)#Trunks (Teen) (Future)"',"").replace('Mai (disambiguation)#Mai (Future)"',"").replace('Beerus (disambiguation)"',"").replace('Krillin (disambiguation)#Krillin"',"").replace('Krillin (disambiguation)#Krillin"',"")

rSphereFile = rExtraDisambig.replace('File:Rainbow icon.png"30px"link=',"").replace('File:Rainbow icon.png"30px','Rainbow').replace('File:AGL icon.png"30px"link=Category:',"").replace('File:AGL  icon.png"30px"link=Category:',"").replace('File:TEQ icon.png"30px"link=Category:',"").replace('File:INT icon.png"30px"link=Category:',"").replace('File: INT icon.png"30px"link=Category:',"").replace('File:STR icon.png"30px"link=Category:',"").replace('File:PHY icon.png"30px"link=Category:',"")

rSSphereFile = rSphereFile.replace('File:SAGL icon.png"30px"link=Category:',"").replace('File:STEQ icon.png"30px"link=Category:',"").replace('File:SINT icon.png"30px"link=Category:',"").replace('File:SSTR icon.png"30px"link=Category:',"").replace('File:SPHY icon.png"30px"link=Category:',"")

rESphereFile = rSSphereFile.replace('File:EAGL icon.png"30px"link=Category:',"").replace('File:ETEQ icon.png"30px"link=Category:',"").replace('File:EINT icon.png"30px"link=Category:',"").replace('File:ESTR icon.png"30px"link=Category:',"").replace('File:EPHY icon.png"30px"link=Category:',"")

rSphereExclude = rESphereFile.replace('icon.png"30px',"")

rStackAtt = rSphereExclude.replace('([[Stack Attack"How does it work?]])',"").replace('Super Attack Multipliers"SA Multiplier',"")

rName1 = rStackAtt.replace(' name="[1]"',"").replace('name=[1]',"").replace('name": [1]',"")
rName2 = rName1.replace(' name="[2]"',"").replace(' name=[2]',"")
rName3 = rName2.replace(' name="[3]"',"").replace(' name=[3]',"")
rName4 = rName3.replace(' name="[4]"',"").replace(' name=[4]',"")
rName5 = rName4.replace(' name="[5]"',"").replace(' name=[5]',"")
rName6 = rName5.replace(' name="[6]"',"").replace(' name=[6]',"")
rName7 = rName6.replace(' name="[7]"',"").replace(' name=[7]',"")
rName8 = rName7.replace(' name="[8]"',"").replace(' name=[8]',"")
rName9 = rName8.replace(' name="[9]"',"").replace(' name=[9]',"")
rName10 = rName9.replace(' name=[10]',"").replace(' name=[10]',"")

rIFrame = rName10.replace('<i>',"").replace('</i>',"")
rRef = rIFrame.replace('<ref>',"  <").replace('<ref >',"  <")
rRef2 = rRef.replace('</ref>',">  ")
rDash = rRef2.replace(' - ',",")
rLB = rDash.replace('[[',"")
rRB = rLB.replace(']]',"")

# ======= this is POST-EDITING print =======
# print(rRB)
test = io.StringIO(rRB)
myline = test.readline()

# start attribute grabbing from cards ==================
extraSpace1 = '{\n'
charSourceLink = (f'"charLinkTo": "{URL2}",\n')
charName1 = ""
charName2 = ""
charRarity = ""
charType = ""
charID = []
charLS = ""
charSaName = []
charSaDesc = []
charUltraName = []
charUltraDesc = []
charPsName = []
charPsDesc = []
charASName = ""
charAS = ""
charASCond = ""
charTransformType = ""
charTransformCond = []
charLinkSkills = []
charCategories = ""
extraSpace2 = '},\n'

while myline:
    myline = test.readline()
    if '"name1": ' in myline:
        charName1 = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"name2":' in myline:
        charName2 = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"rarity":' in myline:
        charRarity = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"type":' in myline:
        charType = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"ID":' in myline:
        charID.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"LS description":' in myline:
        charLS = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"SA name":' in myline:
        charSaName.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"SA description":' in myline:
        charSaDesc.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"UltraSA name":' in myline:
        charUltraName.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"UltraSA description":' in myline:
        charUltraDesc.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"PS name":' in myline:
        charPsName.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"PS description":' in myline:
        charPsDesc.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"Active skill name":' in myline:
        charASName = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Active skill":' in myline:
        charAS = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Active skill condition":' in myline:
        charASCond = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Transform type":' in myline:
        charTransformType = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Transform condition":' in myline:
        charTransformCond.append(myline.replace(': ',': "',1).replace('\n','",\n'))
    if '"Link skill":' in myline:
        charLinkSkills.append(myline.replace(",",'","').replace('" ','"').replace(': ',': ["',1).replace('\n','"],\n'))
    if '"Category":' in myline:
        charCategories = myline.replace(",",'","').replace('" ','"').replace(': ',': ["',1).replace('\n','"]\n')

# start indentation OUT of while loop
# this allows for empty arrays to be filled in so error:'index not found' can be solved
if charSaName == []:
    charSaName = [""]
if charSaDesc == []:
    charSaDesc = [""]
if charUltraName == []:
    charUltraName = [""]
    # print(charUltraName)
if charUltraDesc == []:
    charUltraDesc = [""]
    # print(charUltraDesc)
if charPsName == []:
    charPsName = [""]
if charPsDesc == []:
    charPsDesc = [""]
if charTransformCond == []:
    charTransformCond = [""]
    # print(charTransformCond)
if charLinkSkills == []:
    charLinkSkills = [""]


results = [extraSpace1, charSourceLink, charName1, charName2, charRarity, charType, charID[0], charLS, charSaName[0], charSaDesc[0], charUltraName[0], charUltraDesc[0], charPsName[0], charPsDesc[0], charASName, charAS, charASCond, charTransformType, charTransformCond[0], charLinkSkills[0], charCategories, extraSpace2]
if charLinkSkills[0] == "" or charLinkSkills[0] == "None":
    results = []
if charCategories == []:
    results = []
if '"R"' in charRarity:
    results = []
if '"SR"' in charRarity:
    results = []
if '"SSR"' in charRarity:
    results = []

# this prints everything selected and edited elements, what is put in js file =========
# print(results)
# print('vvvvvv')
# print()
# print('^^^^^')

with open('out.json', 'a', encoding="utf-8") as output:
    output.writelines(results)