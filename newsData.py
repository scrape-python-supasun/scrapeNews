import urllib.request
from bs4 import BeautifulSoup
import re

import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx"

client = MongoClient(uri)
db = client["heroku_2t8dvcnx"]
collections = db['news']

r = urllib.request.urlopen('https://www.ryt9.com/technology-latest/2019-01-08').read()
soup = BeautifulSoup(r ,'html.parser')

# technology__news = soup.find(id="main-category")
def headData():
    listHeadData = []
    
    technologyNewsHead = soup.find_all("h3")
    for element in technologyNewsHead:
        HeadData = element.text
        listHeadData.append(HeadData)
    return listHeadData

# listDataHead = headData()
# print(listDataHead)

def detailData():
    listDetailData = []
    technologyNewsDetail = soup.find_all("p")
    for element in technologyNewsDetail[:-1]:
        detailTextData = element.text
        detailSplitData = detailTextData.split("อ่านต่อ")
        detailFullData = detailSplitData[0]
        listDetailData.append(detailFullData)
    return listDetailData

# listDetailData = detailData()
# print(listDetailData)
# imageAll = image_tag.get('src')

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


def photoDataNameAlt():
    listPhotoName = []
    technologyNewsPhoto = soup.find_all("img")
    for element in technologyNewsPhoto[:-4]:
        photoNewsName= element.get('alt')
        listPhotoName.append(photoNewsName)
    return listPhotoName


def nameHeader():
    headDataDetail = headData()
    photoAlt = photoDataNameAlt()
    allNamePhotoLink = photoLink()
    for element in headDataDetail:
        if element not in photoAlt:
            photoAlt.append(element)
            allNamePhotoLink.append('none')
    return photoAlt


def linknamePhoto():
    headDataDetail = headData()
    photoAlt = photoDataNameAlt()
    allNamePhotoLink = photoLink()
    for element in headDataDetail:
        if element not in photoAlt:
            photoAlt.append(element)
            allNamePhotoLink.append('none')
    return allNamePhotoLink


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
  
    listDetailData = detailData()
    nameAllHeader = nameHeader()
    AllLinkPhoto = linknamePhoto()
    myDictData = {}
    listAllData = []
    for element in range(0,15):
        myDictData = {"id":numberId[element],"Header":nameAllHeader[element],"Detail":listDetailData[element],"photolink":AllLinkPhoto[element]}
        listAllData.append(myDictData)
    return listAllData
allNewsData = allDataNews()
print(allNewsData)


def databaseProfile():
    AllProfile = allDataNews()
    result = collections.insert_many(AllProfile)
    result.inserted_ids
    return result
# ทำให้เข้าถานข้อมูล
# databaseProfileData = databaseProfile()
