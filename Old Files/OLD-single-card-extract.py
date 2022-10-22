from bs4 import BeautifulSoup
import io
import os
import requests


URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Shocking_Absorption_Ability_Buu_(Super)?action=edit")
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

# specified/prepping content ============
rSAType = rQuote.replace('|SA type = Ki',"").replace('|SA type =  Ki',"").replace('|SA Type = Ki',"").replace('|SA type = M',"").replace('|SA type = W',"").replace('|SA type =',"").replace('|UltraSA type = Ki',"").replace('|UltraSA type =  K:',"").replace('|UltraSA type = M',"").replace('|UltraSA type = W',"").replace('|UltraSA type =',"").replace('|SA type Active = Ki',"").replace('|SA type Active = M',"").replace('|SA type Active = W',"").replace('|SA type Active =',"")
rPettan = rSAType.replace('|Pettan = yes',"")
rMoveASCond = rPettan.replace('|Active skill condition','\n|Active skill condition')
rTube = rMoveASCond.replace('|','"')
rEqualSign = rTube.replace(" =",'":')
rLineBreak = rEqualSign.replace('<br>',"").replace('</br>',"")

# further content prunning ================
rServerIcon = rLineBreak.replace('File:Japan server.png"20px',"").replace('File:Global server.png"20px',"")

rExtraCatInLink = rServerIcon.replace('Androids-Cell Saga"',"").replace('Kamehameha (Category)"',"").replace('Otherworld Warriors (Link Skill)"',"").replace('Turtle School (Link Skill)"',"").replace('Namekians (Link Skill)"',"").replace('Team Bardock (Link Skill)"',"").replace(':Category:Extreme Class"',"").replace(':Category:Super Class"',"").replace('Fusion (Link Skill)"',"")

rExtraDisambig = rExtraCatInLink.replace('Goku (disambiguation)"',"").replace('Goku (disambiguation)#Goku"',"").replace('Goku (disambiguation)#Goku (Youth)"',"").replace('Caulifla (disambiguation)"',"").replace('Cooler (disambiguation)"',"").replace('Trunks (disambiguation)"',"").replace('Bardock (disambiguation)"',"").replace('Android 18 (disambiguation)#Android #18"',"").replace('(disambiguation)#Ribrianne"',"").replace('Rozie (disambiguation)"',"").replace('Kakunsa (disambiguation)"',"").replace('Kale (disambiguation)"',"").replace('Tapion (disambiguation)"',"").replace('Gohan (disambiguation)#Gohan (Kid)"',"").replace('Frieza (disambiguation)"',"").replace('Vegeta (disambiguation)"',"").replace('Cooler (disambiguation)#Metal Cooler"',"").replace('Giru (disambiguation)"',"").replace('Cell (disambiguation)"',"").replace('Boujack (disambiguation)"',"").replace('Gohan (disambiguation)#Gohan (Teen)"',"").replace('Gohan (disambiguation)#Ultimate Gohan"',"").replace('Gohan (disambiguation)#Great Saiyaman"',"").replace('Trunks (disambiguation)#Trunks (Kid)"',"").replace('Goten (disambiguation)#Goten (Kid)"',"")

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
charASName = []
charAS = []
charASCond = []
charTransformType = []
charTransformCond = []
charLinkSkills = ""
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
        charID = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"LS description":' in myline:
        charLS = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"SA name":' in myline:
        charSaName = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"SA description":' in myline:
        charSaDesc = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"UltraSA name":' in myline:
        charUltraName = myline.replace(': ',': "',1).replace('\n','",\n')
    if 'UltraSA description:' in myline:
        charUltraDesc = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"PS name":' in myline:
        charPsName = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"PS description":' in myline:
        charPsDesc = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Active skill name":' in myline:
        charASName = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Active skill":' in myline:
        charAS = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Active skill condition":' in myline:
        charASCond = myline.replace(': ',': "',1).replace('\n','",\n')
    if '"Transform type":' in myline:
        charTransformType = myline.replace(': ',': "',1).replace('\n','",\n') 
    if '"Transform condition":' in myline:
        charTransformCond.append(myline.replace(': ',': ["',1).replace('\n','"],\n'))
    if '"Link skill":' in myline:
        charLinkSkills = myline.replace(",",'","').replace('" ','"').replace(': ',': ["',1).replace('\n','"],\n')
    if '"Category":' in myline:
        charCategories = myline.replace(",",'","').replace('" ','"').replace(': ',': ["',1).replace('\n','"]\n')
    

results = [extraSpace1, charSourceLink, charName1, charName2, charRarity, charType, charID, charLS, charSaName, charSaDesc, charUltraName, charUltraDesc, charPsName, charPsDesc, charASName, charAS, charASCond, charTransformType, charTransformCond, charLinkSkills, charCategories, extraSpace2]

if charLS == "":
    results = []
if charCategories == []:
    results = ""
if '"R"' in charRarity:
    results = []
if '"SR"' in charRarity:
    results = []
if '"SSR"' in charRarity:
    results = []

# check before global edits =============
# print(rQuote)
# ======= this is POST-EDITING print =======
# print(rRB)
# prints all pre-edit material...GREAT for finding what needs to be edited for specific cases ============
# print(rLineBreak)
# this prints everything selected and edited elements, what is put in js file =========
# print(results)        

with open('out.json', 'a') as output:
    output.writelines(results)