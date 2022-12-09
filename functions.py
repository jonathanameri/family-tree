import openCSV
import time

#Gather data from openCSV.py
personList = openCSV.personList
dirConList = openCSV.dirConList
connectionDict = openCSV.connectionDict

def printPath(path,short=False):
    curstr = ""
    delim = " -> "
    for name in path:
        if short:
            curstr += name[:5] + delim
        else:
            curstr += name + delim
    curstr = curstr[0:-len(delim)]
    print(curstr)

#Recursive function to traverse graph
def search(p1,p2,myPath,searched,first,possiblePaths,pf=False):
    if True:
        for val in dirConList[p1]:
            # myPath=curPath.copy()
            # If connection is found, print relationship and exit
            if val == p2:
                possiblePaths.append(myPath + [val])
                # print("Searhced[-1]:",searched[-1])
                if(pf): printPath(myPath + [val])
            
        # searched.append(p1)
        for val in dirConList[p1]:
            if (val in personList) and (val not in myPath) and (val not in searched):
                if(pf): printPath(myPath + [val])
                search(val, p2, myPath + [val], searched + [p1], False,possiblePaths)
    else:
        for val in dirConList[p1]:
            # myPath=curPath.copy()
            # If connection is found, print relationship and exit
            if val == p2:
                possiblePaths.append(myPath + [val])
                if(pf): printPath(myPath + [val])
            
            elif (val in personList) and (val not in myPath) and (val not in searched):
                if(pf): printPath(myPath + [val])
                search(val, p2, myPath + [val], searched, False,possiblePaths)

def findShortestPath(possiblePaths,p=False):
    # print(possiblePaths)
    if len(possiblePaths) == 0:
        if(p): print("!!!!!!!!!!!!!!!!!PATH NOT FOUND!!!!!!!!!!!!!!!!!")
        return []
    minLen = len(possiblePaths[0])
    bestPath = possiblePaths[0]
    secondBestPath = []
    for path in possiblePaths:
        if len(path) < minLen:
            minLen = len(path)
            secondBestPath = bestPath
            bestPath = path
    # print("Second best path",secondBestPath)
    if(p): print("Best path:\n")
    if(p): printPath(bestPath)
    if(p): print("")
    if(p): defineRelationship(bestPath)
    return bestPath

def possiblePathsP(possiblePaths):
    print("\n********************Possible Paths********************")
    for path in possiblePaths:
        print(path)

def findRelationship(p1,p2,p=False):
    possiblePaths = []
    curPath = [p1]
    searched = []
    first = True
    if(p): print("------------\nSearching for relationship between " + p1 + " and " + p2 + "\n-------------")
    search(p1,p2,curPath,searched,first,possiblePaths)
    # possiblePathsP(possiblePaths)
    return findShortestPath(possiblePaths)
    
    
def defineRelationship(path):
    relationshipPath = []
    for i in range(len(path)-1):
        relationshipPath.append(connectionDict[(path[i], path[i+1])])
    print(relationshipPath)

def findLongestPath():
    t1 = time.time()
    longestPath = []
    totalIter = len(personList)*len(personList)
    count = 0
    for p1 in personList:
        for p2 in personList:
            path = findRelationship(p1,p2)
            count = count+1
            if len(path) > len(longestPath):
                longestPath = path
            if count % 200 == 0:
                print((100*count/totalIter),"%")
    t2 = time.time()
    print("Took",(t2-t1),"seconds")
    return longestPath

def nameRelationship(rPath):
    if len(rPath) == 0:
        return 'Path is empty'
    relName = rPath[0]
    for i in range(1,len(rPath)-1):

        if rPath[i] == "MOTHER" or rPath[i] == "FATHER":
            rPath[i] = "PARENT"

def findEveryone():
    testPerson = personList[0]
    count = 0
    peopleCount = len(personList)
    cantFind = []
    for i in range(1,peopleCount-1):
        path = findRelationship(testPerson,personList[i])
        if path != []:
            count+= 1
        else:
            cantFind.append(personList[i])
        print(100*(i/peopleCount),"%")
    
    print("Found",count,"out of",peopleCount)
    if count != peopleCount:
        print("Could not find",cantFind)
