import sys
import re
import os
import json
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring
from ElementTree_pretty import prettify
from fileNameList import htmlListFile
from buildtrees import buildSubTree, buildTree
from bs4 import BeautifulSoup
from replace import findAndDeleteCaps, module2replace, module1replace

def getSoup(filename):
    fhand = open(filename, 'r')
    html = fhand.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def getPartTitle(soup):
    title = soup.find('h1')
    titleText = title.get_text()
    return titleText

#takes in the filename of an XML file and returns all the cuepoints from that file in the form [[id, time, src], [id, time, src]]
def getCuePoints(filename):
    cueSoup = getSoup(filename)
    cueList = []
    cuePoints = cueSoup.find('cuepoints')
    for cue in cuePoints.find_all('cuepoint'):
        id = cue['id']
        time = cue['time']
        src = "media/"+cue['src']
        cueList = cueList + [[id, time, src]]
    cueList = [cueList]
    return(cueList)

def getVideoIDWithTimes(strForSearch, videoList, path):
    videoCuePoints = False
    videoID = re.findall(r'1_[0-9a-z]{8}', strForSearch)
    #if not videoID

    videoCuePoints = re.findall(r'media\/[0-9A-Za-z]{2,15}\.xml', strForSearch)
    videoList = [videoID+["PLACEHOLDER"]]
    cuePoints = ""
    if videoCuePoints:
        cuePoints = getCuePoints(path+"/"+videoCuePoints[0])
        videoList = [videoID+["PLACEHOLDER"]+cuePoints]
    else:
        videoList = [videoID+["PLACEHOLDER"]+"NOCUE"]
    return videoList

def getSequenceVideos(soup, path):
    videoList =[]
    s_div = soup.find(id='media-sequence')
    try:
        videoLinks=s_div.find_all('a')
        c = 0
        for item in videoLinks:
            title = item.get_text().strip()
            title = re.sub(r'[\s]+',' ', title)
            videoList = videoList + getVideoIDWithTimes(str(item), videoList, path)
            videoList[c][1] = title
            c+=1
        return videoList
    except:
        pass
    #    print("FAIL Get Sequence Videos")

def getFirstVideo(soup, path):
    try:
        videoList =[]
        player_div = soup.find(id='player')
        playerCall = str(player_div.find('script').contents)
        videoList = getVideoIDWithTimes(playerCall, videoList, path)
        videoList[0][1]=getPartTitle(soup)
        return videoList
    except:
        pass
    #    print("FAIL Get first video")

def getTableVideos(soup, path):
    videoList =[]
    t_div = soup.find(id='media-picker')
    try:
        videoLinks=t_div.find_all('a')
        c = 0
        for item in videoLinks:
            title = item.get_text().strip()
            title = re.sub(r'[\s]+',' ', title)
            videoList = videoList + getVideoIDWithTimes(str(item), videoList, path)
            videoList[c][1] = title
            #adds the "grid" tag for the table
            videoList[c].insert(3,'#')

            c+=1
        return videoList
    except:
        pass
    #    print("FAIL Get Table Videos")

def getMainVideos(soup, path):
    videoList = []
    if getSequenceVideos(soup, path):
        videoList = getSequenceVideos(soup, path)
        with open('videos.txt', 'a') as file:
            for c in videoList:
                file.write(str(c[0])+', '+str(c[1])+'\n')
        return videoList
    elif getTableVideos(soup, path):
        videoList = getTableVideos(soup, path)
        with open('videos.txt', 'a') as file:
            for c in videoList:
                file.write(str(c[0])+', '+str(c[1])+'\n')
        return videoList
    elif getFirstVideo(soup, path):
        videoList= getFirstVideo(soup, path)
        with open('videos.txt', 'a') as file:
            for c in videoList:
                file.write(str(c[0])+', '+str(c[1])+'\n')
        return videoList
    else:
        print(getPartTitle(soup) + " has no videos")
        return videoList

#gets titles and filenames of items in Resources and supplements (id= material-resource, id= material) and returns them as a list [name,src]
def getResources(soup, path):
    mr_div = soup.find(id='material-resource')
    resourceList = []
    if mr_div:
        for resource in mr_div.find_all('a'):
            resourceString = str(resource)
            name = resource.get_text()
            name = re.sub(r'[\s]+',' ', name)
            src = resource['href']
            if re.search(r'1_[0-9a-z]{8}', resourceString ):
                src = src+".vid"
            resourceList = resourceList + [[name, src]]
    return resourceList

def getSupplements(soup, path):
    m_div = soup.find(id='material')
    supplementList =[]
    if m_div:
        for supplement in m_div.find_all('a'):
            suppString = str(supplement)
            name = supplement.get_text()
            name = re.sub(r'[\s]+',' ', name)
            src = supplement['href']
            if re.search(r'1_[0-9a-z]{8}', suppString ):
                src = src+".vid"

            supplementList = supplementList + [[name, src]]
    return supplementList

def writeToFile(partname, XMLdata):
    prettyData = prettify(XMLdata)
    outFile = open(partname, 'w')
    outFile.write(prettyData)
    return True

def videoListPrint(partname, XMLdata):
    prettyData = prettify(XMLdata)
    outFile = open(partname, 'w')
    outFile.write(prettyData)
    return True

def convertFile(fullPath, path):
    soup = getSoup(fullPath)
    title = getPartTitle(soup)
    videos = getMainVideos(soup, path)
    resources = getResources(soup, path)
    supplements = getSupplements(soup, path)
    data = buildTree(resources, supplements, videos)
    #tree = ElementTree(data)
    #tree.write('output.xml')

    newFileName = re.sub(r'html','xml',fullPath)
    writeToFile(newFileName, data)

def buildManifest( PartName, Path, Title):
    with open('/Users/kauwers/Desktop/Module1-2/module_data.xml', 'a') as writeFile:
        session = ET.Element('session')
        session.set('name', "Part "+PartName)
        session.set('path', Path)
        session.set('title', Title)
        prettyData = prettify(session)
        writeFile.write(prettyData)


print("START ==========================+################++++============")

#htmlListFile()

with open('/Users/kauwers/Desktop/Module1-2/fileNameList.json', 'r') as json_file:
    for line in json_file:
        for line in json_file:
            json_path = json.loads(line)
            convertFile(json_path['fullpath'],json_path['path'])
            oldPath = json_path['fullpath']
            #soup = getSoup(json_path['fullpath'])
            #title = getPartTitle(soup)
            #buildManifest(oldPath[-6:-5], oldPath[-11:-5], title)

            newPath = oldPath.replace("html", "xml")
            findAndDeleteCaps(newPath)
            module2replace(newPath)
            module1replace(newPath)
