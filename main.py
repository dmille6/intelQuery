# This is a sample Python script.
from Library import libPullIPLists
from Library import libProcessLists
from Library import libQuery
from pprint import pprint

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fireHolOBJ = libPullIPLists.pullFireHol()
    fireHolOBJ.pullListsFromGit()

    listProcessor = libProcessLists.processLists()

    listProcessor.getFileLists()

    listProcessor.processIPList()
    listProcessor.showIPDict()

    listProcessor.processRangeList()
    listProcessor.showRangeDict()

    QueryObj = libQuery.QueryIP()
    QueryObj.getFileLists()
    QueryObj.showFileList()

    ipDict=listProcessor.getIP()
    rangeDict=listProcessor.getRange()

    QueryObj.readProviderDescriptions()
    QueryObj.QueryIPs(ipDict, rangeDict)
