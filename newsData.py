import urllib.request
from bs4 import BeautifulSoup
import re

import pymongo
from pymongo import MongoClient
uri = "mongodb://heroku_2t8dvcnx:4uamfel6g9rdp2pfuevg0r3t8s@ds153824.mlab.com:53824/heroku_2t8dvcnx"

client = MongoClient(uri)
db = client["heroku_2t8dvcnx"]
collections = db['news']

from datetime import datetime,tzinfo,timedelta

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

datetimeUtc = datetime.utcnow().strftime('%Y-%m-%d')
print("the time is: ",datetimeUtc)

# 
# test commit
#


# list ของเว็บ
category=['world','economy','stock','politics','entertain','sports','travel','technology','real_estate','motor','general']
for topic in category:
    print(topic)
# รวมหน้าเว็บที่เราจะsoupมาsoup
    def scrape(topic):
        website = 'https://www.ryt9.com/{}-latest/{}'.format(topic,datetimeUtc)
        r = urllib.request.urlopen(website).read()
        soup = BeautifulSoup(r ,'html.parser')
        return soup
    # คำสั้งscrape ทั้งหมด
    soup = scrape(topic)
    # print(scrapeLinkAll)
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
    # listDetail = detailData()
    # print(listDetail)

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
    # allphotoDataNameAlt = photoDataNameAlt()
    # print(allphotoDataNameAlt)
# ------------------------------------ข้อความทั้งหมดของวันนี้------------------------------------------------------------------------------
# ข้อความทั้งหมดของวันนี้
    def TextDataDay():
        contentDataAll = soup.find_all(attrs={"id": "main-category"})
        for element in contentDataAll:
            contentAllText = element.text
            contentSplitDay = contentAllText.split('. 20')
            contentToday = contentSplitDay[2]
        return contentToday
    # allTextDataDay = TextDataDay()
    # print(allTextDataDay)
# หัวข้อของวันนี้
    def allHeaderToday():
        allTextDataDay = TextDataDay()
        listDataHead = headData()
        allHeaderToday = []
        for HeaderData in listDataHead:
            if HeaderData in allTextDataDay:
            # print(HeaderData)
                allHeaderToday.append(HeaderData)
        return allHeaderToday
    # allHeaderTodayList = allHeaderToday()
    # print(allHeaderTodayList)
# ซื่อรูปของวันนี้
    def allNamePhotoAltToday():
        listAllHeaderToday = allHeaderToday()
        listPhotoName = photoDataNameAlt()
        allLinkName = []
        for element in listAllHeaderToday:
            if element in listPhotoName:
                allLinkName.append(element)
        return allLinkName
    # allNamePhotoAlt = allNamePhotoAltToday()
    # print(allNamePhotoAlt)
# ลิ้งรูปของวันนี้
    def photoLinkToday():
        allphotoLink = photoLink()
        allNamePhoto = allNamePhotoAltToday()
        allLinkToday = []
        totalNumberLink = len(allNamePhoto)
        allSolutionLink = allphotoLink[:totalNumberLink]
        return allSolutionLink
    # allLinkDataToday = photoLinkToday()    
    # print(allLinkDataToday)
# เนื่อหาของวันนี้
    def allDetailToday():
        allTextDataDay = TextDataDay()
        listDataDetail = detailData()
        
        allDetailToday = []
        for detailDataToday in listDataDetail:
            if detailDataToday in allTextDataDay:
                allDetailToday.append(detailDataToday)
        return allDetailToday
    # allDetailToday = allDetailToday()
    # print(allDetailToday)


# ------------------------------------ข้อความทั้งหมดของวันนี้------------------------------------------------------------------------------
# ซื่อหัวข้อรวมnone
    def nameHeader():
        allHeaderTodayList = allHeaderToday()
        allNamePhotoAlt = allNamePhotoAltToday()
        allLinkDataToday = photoLinkToday()
        for element in allHeaderTodayList:
            if element not in allNamePhotoAlt:
                allNamePhotoAlt.append(element)
                allLinkDataToday.append('none')
        return allNamePhotoAlt
    # nameAllHeader = nameHeader()
    # print(nameAllHeader)

# ซื่อlinkรวมnone
    def linkNamePhoto():
        allHeaderTodayList = allHeaderToday()
        allNamePhotoAlt = allNamePhotoAltToday()
        allLinkDataToday = photoLinkToday()
        for element in allHeaderTodayList:
            if element not in allNamePhotoAlt:
                allNamePhotoAlt.append(element)
                allLinkDataToday.append('nonePhoto')
        return allLinkDataToday
    # listlinkNamePhoto = linkNamePhoto()
    # print(listlinkNamePhoto)
    
# ---------------------------------------------------------------------
# ซื่อรายละเอยีดรวมnone ของวันนี้ โดยที่ยุ้งยากเพราะจำนวนรูปกับเนื้อหาไม่เท้ากัน เลยต้องใช้dictมาช่วย
    def listNameAndDescription():
        allHeaderTodayList = allHeaderToday()
        listAllDetailToday = allDetailToday()
        lengthDataDescriptionToday = len(allHeaderTodayList)
        allListNameAndDetail = []
        dictNameAndDescription = {}
        
        for element in range(0,lengthDataDescriptionToday):
            listDictHeader = {allHeaderTodayList[element]: listAllDetailToday[element]}
            dictNameAndDescription.update(listDictHeader)
        return dictNameAndDescription
    # AllnameDescription = listNameAndDescription()
    # print(AllnameDescription)

    def listNameAndLinkPhoto():
        allNamePhotoAlt = allNamePhotoAltToday()
        listlinkNamePhoto = linkNamePhoto()
        lengthPhoto = len(allNamePhotoAlt)
        dictNamePhoto = {}
        allListPhotoNameAndLink = []
        for element in range(0,lengthPhoto):
            listDictPhoto = {allNamePhotoAlt[element]: listlinkNamePhoto[element]}
            dictNamePhoto.update(listDictPhoto)
        return dictNamePhoto
    # AllNamePhotoAndLinkPhoto = listNameAndLinkPhoto()
    # print(AllNamePhotoAndLinkPhoto)

    def listDescriptionHavePhoto():
        AllnameDescription = listNameAndDescription()
        AllNamePhotoAndLinkPhoto = listNameAndLinkPhoto()
        listDetailHavePhoto = []
        for key, value in AllnameDescription.items():
            if key in AllNamePhotoAndLinkPhoto:
                detailHavePhoto = value
                listDetailHavePhoto.append(detailHavePhoto)
        return listDetailHavePhoto
    # allDescriptionHavePhoto = listDescriptionHavePhoto()
    # print(allDescriptionHavePhoto)
    def listDescriptionNotHavePhoto():
        AllnameDescription = listNameAndDescription()
        AllNamePhotoAndLinkPhoto = listNameAndLinkPhoto()
        listDetailNotHavePhoto = []
        for key, value in AllnameDescription.items():
            if key not in AllNamePhotoAndLinkPhoto:
                detailNotHavePhoto = value
                listDetailNotHavePhoto.append(detailNotHavePhoto)
        return listDetailNotHavePhoto
    # allDescriptionNotHavePhoto = listDescriptionNotHavePhoto()
    # print(allDescriptionNotHavePhoto)
# รวม nonephotoของรายละเอียดเเล้ว ของวันนี้
    def ListDescriptionPhoto():
        allDescriptionHavePhoto = listDescriptionHavePhoto()
        allDescriptionNotHavePhoto = listDescriptionNotHavePhoto()
        lengthNotPhoto = len(allDescriptionNotHavePhoto)
        for element in range(0,lengthNotPhoto):
            allDescriptionHavePhoto.append(allDescriptionNotHavePhoto[element])
        return allDescriptionHavePhoto
    ListDescriptionPhoto()
    # allSolutionDescription = ListDescriptionPhoto()
    # print(allSolutionDescription)


# ---------------------------------------------------------------------


# รวมข้อมูลทั้งหมด
    def allDataNews():
        nameAllHeader = nameHeader()
        AllLinkPhoto = linkNamePhoto()
        allSolutionDescription = ListDescriptionPhoto()
        myDictData = {}
        listAllData = []
        lenghtData = len(allSolutionDescription)
        for element in range(0,lenghtData):
            myDictData = {"Header":nameAllHeader[element],"Detail":allSolutionDescription[element],"photolink":AllLinkPhoto[element],"time":datetimeUtc,"category":topic}
            listAllData.append(myDictData)
        return listAllData
    AllProfile = allDataNews()
    print(AllProfile)


# เข้าถานข้อมูล
    def databaseProfile():
        AllProfile = allDataNews()
        result = collections.insert_many(AllProfile)
        result.inserted_ids
        print('success in create api')
        return result
    # ทำให้เข้าถานข้อมูล
    databaseProfileData = databaseProfile()
