import csv
personList = []
dirConList = dict()         #List of each individual person's 'direct' connections
connectionDict = dict()     #List of each connection and its value

# def removeMiddleName(name):
#     spaceCount = 0
#     spaceIndecies = []
#     for i in range(len(name)-1):
#         if name[i] == ' ':
#             spaceCount+=1
#             spaceIndecies.append(i)
#     if spaceCount == 2:
#         return (name[:spaceIndecies[0]] + name[spaceIndecies[1]:])

with open('./data/familyDataWIP.csv',  newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    nameString = reader.fieldnames[0] #should be the key 'name'

    # for row in reader:
    #     row[nameString] = row[nameString].rstrip()
    #     for connection in ['FATHER','MOTHER','SPOUSE','EX-SPOUSE','CHILD1','CHILD2','CHILD3','CHILD4','CHILD5','CHILD6','CHILD7','CHILD8','CHILD9','CHILD10']:
    #         row[connection] = row[connection].rstrip()
        

    for row in reader:
        currentperson = row[nameString].rstrip()
        # currentperson = currentperson

        # if currentperson[-1] == ' ':
        #     currentperson = currentperson[:-1]

        personList.append(currentperson)
        dirConList[currentperson] = []
        for connection in ['FATHER','MOTHER','SPOUSE','EX-SPOUSE','CHILD1','CHILD2','CHILD3','CHILD4','CHILD5','CHILD6','CHILD7','CHILD8','CHILD9','CHILD10']:
            curCon = row[connection].rstrip()
            # curCon = curCon
            if curCon != '':
                dirConList[currentperson].append(curCon)
                if connection[0] != 'C':
                    connectionDict[(currentperson,curCon)] = connection
                else:
                    connectionDict[(currentperson,curCon)] = 'CHILD'
        

        # for key in row:
        #     for char in key:
        #         if char == "":
        #             print("1")
        #         print(char)
        #     if key == "\nname":
        #         print("SUCCESS")
        #     exit()
        #     print(key)

        # # print(row['NAME'])