import os
import sys
import shutil
from tqdm import tqdm
from pprint import pprint

class QueryIP:
    outputFolder= "./Completed/"
    queryFileList = []
    tagDescDict = {}
    def __init__(self):
        print ("QueryIP Object Created")

    def getFileLists(self):
        for file in tqdm(os.listdir("./ToProcess")):
            if file:
                strFilename = os.path.join("./ToProcess", file)
                if ".txt" in strFilename:
                    self.queryFileList.append(strFilename)
                else:
                    print ("Not Important:", strFilename)

    def showFileList(self):
        pprint (self.queryFileList)

    def readProviderDescriptions(self):
        with open("./Library/firehol_tag_descriptions.csv", "r") as filehandler:
            for line in filehandler:
                # try:
                if line[0] != "#":
                    line = line.replace("\n", "")
                    tagAndDescList=line.split(",",1)
                    tagAndDescList[1]=tagAndDescList[1].replace('"','')
                    tagAndDescList[1] = tagAndDescList[1].replace('\xa0', ': ')

                    self.tagDescDict[tagAndDescList[0]]=tagAndDescList[1]
        #pprint (self.tagDescDict)

    def QueryIPs(self, IPDict, RangeDict):
        for file in self.queryFileList:
            strFilename=file
            strFilename=strFilename.replace("./ToProcess/","")
            outputFile=self.outputFolder+strFilename
            outputFile=outputFile.replace(".txt","_results.txt")

            print ("::", outputFile)
            print ("\n")
            print ("---========= ",strFilename, " ===========---")
            file_writer=open(outputFile,"w")
            lineToWrite=strFilename + "\n"
            file_writer.write(lineToWrite)
            with open(file, "r") as filehandler:
                for line in filehandler:
                    try:
                        if line[0] != "#":
                            line=line.replace("\n","")
                            if line in IPDict.keys():
                                print ("IP:", line, " Found :", IPDict[line])
                                lineToWrite="  IP:" +  str(line) +  " Found :" +  str(IPDict[line])+"\n"
                                file_writer.write(lineToWrite)
                                for item in IPDict[line]:
                                    print ("   --:", item," : ", self.tagDescDict[item] )
                                    lineToWrite="   --:" + str(item) + " : " +  str(self.tagDescDict[item]) + "\n"
                                    file_writer.write(lineToWrite)
                    except:
                        e = sys.exc_info()[0]
                        print("ERROR:", e)
                        errorString = "LoadFile ERROR: " + line + " : " + str(e) + "\n"
                        # pprint.pprint(self.deDupedDict)

            file_writer.close()
            shutil.move(file, self.outputFolder)


