import os
from os.path import join, getsize
import json
import re

def htmlListFile():
    a = {}
    for root, dirs, files in os.walk('/Users/kauwers/Desktop/Module1-2/Modules'):
        for name in files:
            if re.search('library',os.path.join(root, name)):
                pass
            elif name.endswith((".html", ".htm")):
                a['fullpath'] = os.path.join(root, name)
                a['path']=root
                with open('/Users/kauwers/Desktop/Module1-2/fileNameList.json','a') as fp:
                    json.dump(a, fp)
                    fp.write("\n")
    fp.close()
    return True

#need to make this write to JSON and store the filename and also containing folder path, to replace with "media" in the timing script
