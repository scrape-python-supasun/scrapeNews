import urllib.request
from bs4 import BeautifulSoup
import re

import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx"

client = MongoClient(uri)
db = client["heroku_2t8dvcnx"]
collections = db['news']

time = input('what is time(Year-Month-Day): ')
print('the time is: ',time)
category = input('what is category: ')
print('the category is: ',category)


website = 'https://www.ryt9.com/{}-latest/{}'.format(category,time)
r = urllib.request.urlopen(website).read()
soup = BeautifulSoup(r ,'html.parser')

# หัวข้อ
def headData():
    listHeadData = []
    
    technologyNewsHead = soup.find_all("h3")
    for element in technologyNewsHead:
        HeadData = element.text
        listHeadData.append(HeadData)
    return listHeadData

# listDataHead = headData()
# print(listDataHead)
# รายละเอยีด
def detailData():
    listDetailData = []
    technologyNewsDetail = soup.find_all("p")
    for element in technologyNewsDetail[:-1]:
        detailTextData = element.text
        detailSplitData = detailTextData.split("อ่านต่อ")
        detailFullData = detailSplitData[0]
        listDetailData.append(detailFullData)
    return listDetailData

# ลิ้งรูป
def photoLink():
    listLinkPhoto = []
    technologyLinkPhoto = soup.find_all("img")
    for element in technologyLinkPhoto[:-4]:
        photoNews = element.get('src')
        photoSplit = photoNews.split('https://i.ryt9.com/sc,120x120/')
        photoAllLink = photoSplit[1]
        listLinkPhoto.append(photoAllLink)
    return listLinkPhoto
# allphotoLink = photoLink()
# print(allphotoLink)

# ซื่อของรูป
def photoDataNameAlt():
    listPhotoName = []
    technologyNewsPhoto = soup.find_all("img")
    for element in technologyNewsPhoto[:-4]:
        photoNewsName= element.get('alt')
        listPhotoName.append(photoNewsName)
    return listPhotoName

# ซื่อหัวข้อรวมnone
def nameHeader():
    headDataDetail = headData()
    photoAlt = photoDataNameAlt()
    allNamePhotoLink = photoLink()
    for element in headDataDetail:
        if element not in photoAlt:
            photoAlt.append(element)
            allNamePhotoLink.append('none')
    return photoAlt
# b = nameHeader()
# print(b)
# print('\n')


# ซื่อlinkรวมnone
def linknamePhoto():
    headDataDetail = headData()
    photoAlt = photoDataNameAlt()
    allNamePhotoLink = photoLink()
    for element in headDataDetail:
        if element not in photoAlt:
            photoAlt.append(element)
            allNamePhotoLink.append('nonePhoto')
    return allNamePhotoLink
# a = linknamePhoto()
# print(a)
# print('\n')
# รายละเอียดรวมnone
def detailNameAll():
    headDataDetail = headData()
    photoAlt = photoDataNameAlt()
    allNamePhotoLink = photoLink()
    detailNews = detailData()
    # listData=[]
    for element in headDataDetail:
        if element not in photoAlt:
            # print(element)
            allList = headDataDetail
            ListPosition = allList.index((element))
            del detailNews[ListPosition]
            detailNews.append('noneDetail')
    return detailNews
# c = detailNameAll()
# print(c)



def idNumber():
    allNumber = []
    for element in range(1,16):
        number = element
        allNumber.append(number)
    return allNumber
# numberId = idNumber()
# print(numberId)

def allDataNews():
    numberId = idNumber()

    nameAllHeader = nameHeader()
    AllLinkPhoto = linknamePhoto()
    listdetailAll = detailNameAll()
    myDictData = {}
    listAllData = []
    for element in range(0,15):
        # myDictData = {"id":numberId[element],"Header":nameAllHeader[element],"Detail":listdetailAll[element],"photolink":AllLinkPhoto[element],"time":time,"category":category}
        myDictData = {"id":numberId[element],"Header":nameAllHeader[element],"Detail":listdetailAll[element],"photolink":AllLinkPhoto[element],"time":time,"category":category}

        listAllData.append(myDictData)
        # print('\n')
    return listAllData
# allNewsData = allDataNews()
# print(allNewsData)


def databaseProfile():
    AllProfile = allDataNews()
    result = collections.insert_many(AllProfile)
    result.inserted_ids
    return result
# ทำให้เข้าถานข้อมูล
databaseProfileData = databaseProfile()
