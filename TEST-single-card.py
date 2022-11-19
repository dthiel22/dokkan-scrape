from bs4 import BeautifulSoup
import io
import requests

# URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Pinnacle_of_Fury_Goku?action=edit")
# URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Ultimate_Life_Form_with_Immense_Power_Cell_(1st_Form)?action=edit")
# URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Devastating_Punishment_Beerus?action=edit")
# URL2 = ("https://dbz-dokkanbattle.fandom.com/wiki/Shocking_Absorption_Ability_Buu_(Super)?action=edit")

# COPY HERE FOR SCRAPE ALL
URL2 = (
    f"https://dbz-dokkanbattle.fandom.com/wiki/Glorious_Battle_Super_Saiyan_Trunks_(Kid)?action=edit")
print(URL2)

print("=============================== main card page ===============================")
# grabbing main part of dokkan page + text box ========
linkUsed = requests.get(URL2)
main = BeautifulSoup(linkUsed.content, "html.parser")
content = main.find(id="mw-content-text")
textBoxEl = content.find(id='wpTextbox1').text

# check before global edits =============
print('')
# print(textBoxEl)

# specified/prepping content ============
rQuote = textBoxEl.replace('"', "")
rSAName = rQuote.replace('|SA name', "\n|SA name").replace(
    '|UltraSA name', "\n|UltraSA name")
rPettan = rSAName.replace('|Pettan = yes', "")
rMoveASCond = rPettan.replace('|Active skill condition', '\n|Active skill condition').replace(
    '|Active skill name', '\n|Active skill name')
rEqualSign = rMoveASCond.replace(" =", ':')
rLineBreak = rEqualSign.replace('<br>', "").replace('</br>', "")

# prints all pre-edit material...GREAT for finding what needs to be edited for specific cases ============
# print(rLineBreak)

# further content prunning ================
rServerIcon = rLineBreak.replace('File:Japan server.png|20px', "").replace(
    'File:Global server.png|20px', "")

rExtraCatInLink = rServerIcon.replace('Androids-Cell Saga|', "").replace('Kamehameha (Category)|', "").replace('Otherworld Warriors (Link Skill)|', "").replace('Turtle School (Link Skill)|', "").replace(
    'Namekians (Link Skill)|', "").replace('Team Bardock (Link Skill)|', "").replace(':Category:Extreme Class|', "").replace(':Category:Super Class|', "").replace('Fusion (Link Skill)|', "")

rExtraDisambig = rExtraCatInLink.replace('Goku (disambiguation)|', "").replace('Goku (disambiguation)#Goku|', "").replace('Goku (disambiguation)#Goku (Angel)|', "").replace('Goku (disambiguation)#Super Saiyan Goku|', "").replace('Goku (disambiguation)#Goku (Youth)|', "").replace('Caulifla (disambiguation)|', "").replace('Cooler (disambiguation)|', "").replace('Trunks (disambiguation)|', "").replace('Bardock (disambiguation)|', "").replace('Android 18 (disambiguation)|', '').replace('Android 18 (disambiguation)#Android #18|', "").replace('(disambiguation)#Ribrianne|', "").replace('Rozie (disambiguation)|', "").replace('Kakunsa (disambiguation)|', "").replace('Kale (disambiguation)|', "").replace('Tapion (disambiguation)|', "").replace('Gohan (disambiguation)#Gohan (Kid)|', "").replace('Frieza (disambiguation)|', "").replace('Vegeta (disambiguation)|', "").replace('Cooler (disambiguation)#Metal Cooler|', "").replace('Giru (disambiguation)|', "").replace('Cell (disambiguation)|', "").replace('Boujack (disambiguation)|', "").replace('Gohan (disambiguation)#Gohan (Teen)|', "").replace('Gohan (disambiguation)#Ultimate Gohan|', "").replace('Gohan (disambiguation)#Great Saiyaman|', "").replace('Gohan (disambiguation)#Gohan (Future)|', "").replace('Trunks (disambiguation)#Trunks (Kid)|', "").replace('Trunks (disambiguation)#Trunks (Teen)|', "").replace('Goten (disambiguation)#Goten (Kid)|', "").replace('Piccolo (disambiguation)|', '').replace('Piccolo (disambiguation)#Piccolo|', "").replace('Cell (disambiguation)#Cell (Perfect Form)|', "").replace('Cell (disambiguation)#Perfect Cell|', "").replace('Gohan (disambiguation)#Super Saiyan Gohan (Youth)|', "").replace('Gohan (disambiguation)#Super Saiyan 2 Gohan (Youth)|', "").replace('Android 14 (disambiguation)#Androids #14 & #15|', "").replace('Android 16 (disambiguation)|', "").replace('Android 17 (disambiguation)#Android #17|', "").replace('Android 17 (disambiguation)|#17', "").replace('Android 18 (disambiguation)#Android #18 (Future)|', "").replace('Android 17 (disambiguation)#Android #17 (Future)|', "").replace('Ginyu (disambiguation)|', "").replace('Android 13 (disambiguation)#Android #13|', "").replace('Android 13 (disambiguation)#Fusion Android #13|', "").replace('Zamasu (disambiguation)#Zamasu|', "").replace('Zamasu (disambiguation)#Goku Black|', "").replace('Trunks (disambiguation)#Trunks (Teen) (Future)|', "").replace('Mai (disambiguation)#Mai (Future)|', "").replace('Beerus (disambiguation)|', "").replace('Krillin (disambiguation)#Krillin|', "").replace('Krillin (disambiguation)|Krillin', "").replace('Bulma (disambiguation)|', "").replace('Bulma (disambiguation)#Bulma (Youth)|', "")

rSphereFile = rExtraDisambig.replace('File:Rainbow icon.png|30px|link=', "").replace('File:Rainbow icon.png|30px', 'Rainbow').replace('File:AGL icon.png|30px|link=Category:', "").replace('File:AGL  icon.png|30px|link=Category:', "").replace(
    'File:TEQ icon.png|30px|link=Category:', "").replace('File:INT icon.png|30px|link=Category:', "").replace('File: INT icon.png|30px|link=Category:', "").replace('File:STR icon.png|30px|link=Category:', "").replace('File:PHY icon.png|30px|link=Category:', "").replace('File: PHY icon.png|30px|link=Category:PHY', '')

rSSphereFile = rSphereFile.replace('File:SAGL icon.png|30px|link=Category:', "").replace('File:STEQ icon.png|30px|link=Category:', "").replace(
    'File:SINT icon.png|30px|link=Category:', "").replace('File:SSTR icon.png|30px|link=Category:', "").replace('File:SPHY icon.png|30px|link=Category:', "")

rESphereFile = rSSphereFile.replace('File:EAGL icon.png|30px|link=Category:', "").replace('File:ETEQ icon.png|30px|link=Category:', "").replace(
    'File:EINT icon.png|30px|link=Category:', "").replace('File:ESTR icon.png|30px|link=Category:', "").replace('File:EPHY icon.png|30px|link=Category:', "")

rSphereExclude = rESphereFile.replace('icon.png|30px', "")

rStackAtt = rSphereExclude.replace('([[Stack Attack|How does it work?]])', "").replace(
    'Super Attack Multipliers|SA Multiplier', "super attack")

rName1 = rStackAtt.replace(' name="[1]"', "").replace(
    'name=[1]', "").replace('name": [1]', "").replace('name":[1]', "")
rName2 = rName1.replace(' name="[2]"', "").replace(
    ' name=[2]', "").replace('name": [2]', "").replace('name":[2]', "")
rName3 = rName2.replace(' name="[3]"', "").replace(
    ' name=[3]', "").replace('name": [3]', "").replace('name":[3]', "")
rName4 = rName3.replace(' name="[4]"', "").replace(
    ' name=[4]', "").replace('name": [4]', "").replace('name":[4]', "")
rName5 = rName4.replace(' name="[5]"', "").replace(
    ' name=[5]', "").replace('name": [5]', "").replace('name":[5]', "")
rName6 = rName5.replace(' name="[6]"', "").replace(
    ' name=[6]', "").replace('name": [6]', "").replace('name":[6]', "")
rName7 = rName6.replace(' name="[7]"', "").replace(
    ' name=[7]', "").replace('name": [7]', "").replace('name":[7]', "")
rName8 = rName7.replace(' name="[8]"', "").replace(
    ' name=[8]', "").replace('name": [8]', "").replace('name":[8]', "")
rName9 = rName8.replace(' name="[9]"', "").replace(
    ' name=[9]', "").replace('name": [9]', "").replace('name":[9]', "")
rName10 = rName9.replace(' name=[10]', "").replace(
    ' name=[10]', "").replace('name": [10]', "").replace('name":[10]', "")

rIFrame = rName10.replace('<i>', "").replace('</i>', "")
rRef = rIFrame.replace('<ref>', "  <").replace('<ref >', "  <")
rRef2 = rRef.replace('</ref>', ">  ")
rDash = rRef2.replace(' - ', ",")
rLB = rDash.replace('[[', "")
rRB = rLB.replace(']]', "")

# ======= this is POST-EDITING print =======
# print(rRB)
test = io.StringIO(rRB)
myline = test.readline()

# start attribute grabbing from cards ==================
extraSpace1 = '{\n'
charSourceLink = (f'char_link: "{URL2}",\n').replace('?action=edit', "")
charName1 = []
charName2 = []
charRarity = []
charType = []
charCost = []
charID = []
charLS = []
charLSEza = []
charSaType = []
charSaName = []
charSaDesc = []
charSaDescEza = []
charUltraName = []
charUltraDesc = []
charUltraDescEza = []
charPsName = []
charPsDesc = []
charPsDescEza = []
charASType = []
charASName = []
charAS = []
charASCond = []
charASCondEza = []
charTransformType = []
charTransformCond = []
charTransformCondEza = []
charLinkSkills = []
charCategories = []
charJPDate = []
charGLBDate = []
charJPDateEza = []
charGLBDateEza = []
extraSpace2 = '},\n'

linkSeed = ''
categorySeed = ''
idSeed = ''

while myline:
    myline = test.readline()
    if '|name1: ' in myline:
        charName1.append(myline.replace('|', '').replace("name1", "title").replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|name2:' in myline:
        charName2.append(myline.replace('|', '').replace("name2", "name").replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|rarity:' in myline:
        charRarity.append(myline.replace('|', '').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|type:' in myline:
        charType.append(myline.replace('|', '').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|cost:' in myline:
        charCost.append(myline.replace('|', '').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|ID:' in myline:
        charID.append(myline.replace('|', '').replace('ID', 'id').replace(': ', ': ', 1).replace('\n', ',\n'))
    if '|LS description:' in myline:
        charLS.append(myline.replace('|', '').replace("LS description", "ls_description").replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|LS description Z:' in myline:
        charLSEza.append(myline.replace('|', '').replace("LS description Z", "ls_description_eza").replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|SA type:' in myline:
        charSaType.append(myline.replace('|', '').replace('SA type', 'sa_type').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|SA name:' in myline:
        charSaName.append(myline.replace('|', '').replace('SA name', 'sa_name').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|SA description:' in myline:
        charSaDesc.append(myline.replace('|', '').replace('SA description', 'sa_description').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|SA description Z:' in myline:
        charSaDescEza.append(myline.replace('|', '').replace('SA description Z', 'sa_description_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|UltraSA name:' in myline:
        charUltraName.append(myline.replace('|', '').replace('UltraSA name', 'ultra_sa_name').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|UltraSA description:' in myline:
        charUltraDesc.append(myline.replace('|', '').replace('UltraSA description', 'ultra_sa_description').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|UltraSA description Z:' in myline:
        charUltraDescEza.append(myline.replace('|', '').replace('UltraSA description Z', 'ultra_sa_description_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|PS name:' in myline:
        charPsName.append(myline.replace('|', '').replace('PS name', 'ps_name').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|PS description:' in myline:
        charPsDesc.append(myline.replace('|', '').replace('PS description', 'ps_description').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|PS description Z:' in myline:
        charPsDescEza.append(myline.replace('|', '').replace('PS description Z', 'ps_description_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|SA type Active:' in myline:
        charASType.append(myline.replace('|', '').replace('SA type Active', 'sa_type_active').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Active skill name:' in myline:
        charASName.append(myline.replace('|', '').replace('Active skill name', 'active_skill_name').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Active skill:' in myline:
        charAS.append(myline.replace('|', '').replace('Active skill', 'active_skill').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Active skill condition:' in myline:
        charASCond.append(myline.replace('|', '').replace('Active skill condition', 'active_skill_condition').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Active skill condition Z:' in myline:
        charASCondEza.append(myline.replace('|', '').replace('Active skill condition Z', 'active_skill_condition_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Transform type:' in myline:
        charTransformType.append(myline.replace('|', '').replace('Transform type', 'transform_type').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Transform condition:' in myline:
        charTransformCond.append(myline.replace('|', '').replace('Transform condition', 'transform_condition').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Transform condition Z:' in myline:
        charTransformCondEza.append(myline.replace('|', '').replace('Transform condition Z', 'transform_condition_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|Link skill:' in myline:
        charLinkSkills.append(myline.replace('|', '').replace('Link skill', 'link_skill').replace(",", '","').replace('" ', '"').replace(': ', ': ["', 1).replace('\n', '"],\n'))
        linkSeed = myline.replace('|Link skill: ', '')
    if '|Category:' in myline:
        charCategories.append(myline.replace('|', '').replace('Category', 'category').replace(",", '","').replace('" ', '"').replace(': ', ': ["', 1).replace('\n', '"],\n'))
        categorySeed = myline.replace('|Category: ','')
    if '|JPdate: ' in myline:
        charJPDate.append(myline.replace('|', '').replace('JPdate', 'jp_date').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|GLBdate: ' in myline:
        charGLBDate.append(myline.replace('|', '').replace('GLBdate', 'glb_date').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|JPdateEZA: ' in myline:
        charJPDateEza.append(myline.replace('|', '').replace('JPdateEZA', 'jp_date_eza').replace(': ', ': "', 1).replace('\n', '",\n'))
    if '|GLBdateEZA: ' in myline:
        charGLBDateEza.append(myline.replace('|', '').replace('GLBdateEZA', 'glb_date_eza').replace(': ', ': "', 1).replace('\n', '"\n'))

if charName1 == []:
    charName1 = ['title: null,\n']
if charName2 == []:
    charName2 = ['name: null,\n']
if charRarity == []:
    charRarity = ['rarity: null,\n']
if charType == []:
    charType = ['type: null,\n']
if charCost == []:
    charCost = ['cost: null,\n']
if charID == []:
    charID = ['dokkan_id: null,\n']
if charLS == []:
    charLS = ['ls_description: null,\n']
if charLSEza == []:
    charLSEza = ['ls_description_eza: null,\n']
if charSaType == []:
    charSaType = ['sa_type: null,\n']
if charSaName == []:
    charSaName = ['sa_name: null,\n']
if charSaDesc == []:
    charSaDesc = ['sa_description: null,\n']
if charSaDescEza == []:
    charSaDescEza = ['sa_description_eza: null,\n']
if charUltraName == []:
    charUltraName = ['ultra_sa_name: null,\n']
if charUltraDesc == []:
    charUltraDesc = ['ultra_sa_description: null,\n']
if charUltraDescEza == []:
    charUltraDescEza = ['ultra_sa_description_eza: null,\n']
if charPsDescEza == []:
    charPsDescEza = ['ps_description_eza: null,\n']
if charPsName == []:
    charPsName = ['ps_name: null,\n']
if charPsDesc == []:
    charPsDesc = ['ps_description: null,\n']
if charPsDescEza == []:
    charPsDescEza = ['ps_description_eza: null,\n']
if charASType == []:
    charASType = ['sa_type_active: null,\n']
if charASName == []:
    charASName = ['active_skill_name: null,\n']
if charAS == []:
    charAS = ['active_skill: null,\n']
if charASCond == []:
    charASCond = ['active_skill_condition: null,\n']
if charASCondEza == []:
    charASCondEza = ['active_skill_condition_eza: null,\n']
if charTransformType == []:
    charTransformType = ['transform_type: null,\n']
if charTransformCond == []:
    charTransformCond = ['transform_condition: null,\n']
if charTransformCondEza == []:
    charTransformCondEza = [
        'transform_condition_eza: null,\n']
if charLinkSkills == []:
    charLinkSkills = ['link_skill: null,\n']
if charCategories == []:
    charCategories = ['category: null,\n']
if charJPDate == []:
    charJPDate = ['jp_date: null,\n']
if charGLBDate == []:
    charGLBDate = ['glb_date: null,\n']
if charJPDateEza == []:
    charJPDateEza = ['jp_date_eza: null,\n']
if charGLBDateEza == []:
    charGLBDateEza = ['glb_date_eza: null\n']

results = [extraSpace1, charID[0], charSourceLink, charName1[0], charName2[0], charRarity[0], charType[0], charCost[0], charLS[0], charLSEza[0], charSaType[0], charSaName[0], charSaDesc[0], charSaDescEza[0], charUltraName[0],
        charUltraDesc[0], charUltraDescEza[0], charPsName[0], charPsDesc[0], charPsDescEza[0], charASType[0], charASName[0], charAS[0], charASCond[0], charASCondEza[0], charTransformType[0], charTransformCond[0], charTransformCondEza[0], charJPDate[0], charGLBDate[0], charJPDateEza[0], charGLBDateEza[0], extraSpace2]

if charPsName[0] == 'ps_name: null,':
    results = []
if "None" in charLinkSkills[0] or charLinkSkills[0] == 'link_skill: null,':
    results = []
if charCategories[0] == 'category: null,':
    results = []
if '"N"' in charRarity[0]:
    results = []
if '"R"' in charRarity[0]:
    results = []
if '"SR"' in charRarity[0]:
    results = []
if '"SSR"' in charRarity[0]:
    results = []
if '"ItemSSR"' in charRarity[0]:
    results = []

# with open('Characters.json', 'a', encoding="utf-8") as output:
#     output.writelines(results)

idSeed = charID[0]
categoryArr = categorySeed.split(',')
categoryResults = []
for singleCategory in categoryArr:
    categoryResults.append('{\n')
    categoryResults.append('CharacterId: '+idSeed.replace('id: ','').replace('\n', '')+'\n')
    categoryResults.append('CategoryName: '+'"'+singleCategory.replace('\n', '')+'"')
    categoryResults.append('\n},\n')

if charPsName[0] == 'ps_name: null,':
    categoryResults = []
if "None" in charLinkSkills[0] or charLinkSkills[0] == 'link_skill: null,':
    categoryResults = []
if charCategories[0] == 'category: null,':
    categoryResults = []
if '"N"' in charRarity[0]:
    categoryResults = []
if '"R"' in charRarity[0]:
    categoryResults = []
if '"SR"' in charRarity[0]:
    categoryResults = []
if '"SSR"' in charRarity[0]:
    categoryResults = []
if '"ItemSSR"' in charRarity[0]:
    categoryResults = []

# with open('CharacterCategory.js', 'a', encoding="utf-8") as output:
#     output.writelines(categoryResults)

# print(linkSeed)
linkArr = linkSeed.split(',')
print(linkArr)
linkResults = []
for singleCategory in linkArr:
    linkResults.append('{\n')
    linkResults.append('CharacterId: '+idSeed.replace('id: ','').replace('\n', '')+'\n')
    linkResults.append('LinkSkillName: '+'"'+singleCategory.replace('\n', '')+'"')
    linkResults.append('\n},\n')

if charPsName[0] == 'ps_name: null,':
    linkResults = []
if "None" in charLinkSkills[0] or charLinkSkills[0] == 'link_skill: null,':
    linkResults = []
if charCategories[0] == 'category: null,':
    linkResults = []
if '"N"' in charRarity[0]:
    linkResults = []
if '"R"' in charRarity[0]:
    linkResults = []
if '"SR"' in charRarity[0]:
    linkResults = []
if '"SSR"' in charRarity[0]:
    linkResults = []
if '"ItemSSR"' in charRarity[0]:
    linkResults = []

with open('CharacterLink.js', 'w', encoding="utf-8") as output:
    output.writelines(linkResults)