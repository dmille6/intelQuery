import os
import sys
from pprint import pprint
from tqdm import tqdm

class processLists:

    ipBlockList={}
    ipRangeList={}

    ipFileList=[]
    rangeFileList=[]

    def __init__(self):
        print ("Process Lists Object Created")

    def getFileLists(self):
        for file in tqdm(os.listdir("./blocklist-ipsets")):
            if file:
                # strFilename=os.path.join("/data/tpotLogs/Processing/", file) # for production
                strFilename = os.path.join("./blocklist-ipsets", file)
                if ".ipset" in strFilename:
                    self.ipFileList.append(strFilename)
                elif ".netset" in strFilename:
                    self.rangeFileList.append(strFilename)
                #else:
                #    print ("Not Important:", strFilename)

    def processIPList(self):
        for file in self.ipFileList:
            #print (file)

            #print("Reading and Processing:", file)
            #print ("FILE", file)
            with open(file, "r") as filehandler:
                for line in filehandler:
                    try:
                        if line[0] != "#":
                            line=line.replace("\n","")
                            self.addToIPDict(line, file)
                    except:
                        e = sys.exc_info()[0]
                        print("ERROR:", e)
                        errorString = "LoadFile ERROR: " + line + " : " + str(e) + "\n"
                        # pprint.pprint(self.deDupedDict)

    def addToIPDict(self, address, file):
        tag = file
        tag = tag.replace("./blocklist-ipsets/", "")
        tag = tag.replace(".ipset", "")
        tagArray=[]

        if address in self.ipBlockList.keys(): #already found, add new tag
            self.ipBlockList[address].append(tag)
        else:
            tagArray.append(tag)
            self.ipBlockList[address]=tagArray.copy()


    def showIPDict(self):
        #pprint (self.ipBlockList)
        print ("Number of Keys:", len(self.ipBlockList.keys()))


    def processRangeList(self):
        for file in self.rangeFileList:
            #print (file)

            #print("Reading and Processing:", file)
            #print ("FILE", file)
            with open(file, "r") as filehandler:
                for line in filehandler:
                    #try:
                    if line[0] != "#":
                        line=line.replace("\n","")
                        self.addToRangeDict(line, file)
                    #except:
                    #    e = sys.exc_info()[0]
                    #    print("ERROR:", e, "  : ", line)
                    #    errorString = "LoadFile ERROR: " + line + " : " + str(e) + "\n"
                    #    # pprint.pprint(self.deDupedDict)

    def addToRangeDict(self, address, file):
        tag = file
        tag = tag.replace("./blocklist-ipsets/", "")
        tag = tag.replace(".netset", "")
        tagArray=[]
        if address in self.ipBlockList.keys(): #already found, add new tag
            self.ipRangeList[address]=tagArray.append(tag)
        else:
            tagArray.append(tag)
            self.ipRangeList[address]=tagArray.copy()

    def showRangeDict(self):
        #pprint (self.ipRangeList)
        print ("Number of Keys:", len(self.ipRangeList.keys()))

    def getIP(self):
        return self.ipBlockList.copy()

    def getRange(self):
        return self.ipRangeList.copy()




