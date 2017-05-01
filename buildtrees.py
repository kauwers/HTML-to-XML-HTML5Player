import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from xml.etree.ElementTree import ElementTree, Element, SubElement, tostring


def buildSubTree(resources, supplements, cuepoints, video, data,item):
    cuepointsXML = ET.SubElement(video, 'cuepoints')
    try:
        for item in cuepoints:
            cuepoint = ET.SubElement(cuepointsXML, 'cuepoint')
            cuepoint.set('Aid', item[0])
            cuepoint.set('Btime', item[1])
            cuepoint.set('Csrc', item[2])
            print('success', item)
            ET.dump(cuepoint)
    except:
        print('FAIL:  buildSubTree, cuepoints ', item)
    #list of two item tuples (resources)[name,src] and adds those items to the tree
    resourcesXML = ET.SubElement(video, 'resources')
    c = 1
    try:
        for item in resources:
            resource = ET.SubElement(resourcesXML, 'resource')
            resource.set('Aid', str(c))
            resource.set('Bname', item[0])
            resource.set('Csrc', item[1])
            c+=1
    except:
    #    print('FAIL:  buildSubTree, resources')
        pass
    supplementXML = ET.SubElement(video, 'supplements')
    c = 1
    try:
        for item in supplements:
            supplement = ET.SubElement(supplementXML, 'supplement')
            supplement.set('Aid', str(c))
            supplement.set('Bname', item[0])
            supplement.set('Csrc', item[1])
            c+=1
    except:
    #    print('FAIL:  buildSubTree, supplements')
        pass
    return video

def buildTree(resources, supplements, videos):
    data = ET.Element('data')
    try:
        c=0
        for item in videos:
            video = ET.SubElement(data, 'video')
            if c==0:
                relatedvideosXML = ET.SubElement(video, 'relatedvideos')
                for item2 in videos:
                    relate = ET.SubElement(relatedvideosXML, 'relate')
                    relate.set('Aid', item2[0])
                    relate.set('Btitle', item2[1])
                    relate.set('Cthumbnail', "#")
                    relate.set('Dcontent', "#")
            c+=1
        #    print('sub tree item ', item)
            video.set('Aid', item[0])
            video.set('Btitle', item[1])
            video.set('Cthumbnail', "#")
            video.set('Dcontent', "#")
            #buildSubTree(resources, supplements, cuepoints, video, data):
            buildSubTree(resources, supplements, item[2], video, data,item)
    except:
    #    print('FAIL:  buildTree')
        pass
    return data
