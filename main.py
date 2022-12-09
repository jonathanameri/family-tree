import sys
from functions import *

#INPUTS
pf = False           #DEBUG FLAG variable
short = False          #variable if we want to print shortened names
p = False           #variable if we want to print at all
p1 = "Jonathan Ameri"
p2 = "Naomi Glickman"

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("Must have at least one argument\nUsage:\n'Python3 main.py [-] [def] [pList] [lp] [dir + name]")
        exit()
    elif args[1] == '-':
        if args[2] == "pList":
            print(personList)
            exit()
        elif args[2] == "def":
            printPath(findRelationship(p1,p2))
            exit()
        elif args[2] == "lp":
            lp = findLongestPath()
            printPath(lp)
            defineRelationship(lp)
        elif args[2] == "full":
            findEveryone()
        elif args[2] == "dir":
            person = args[3] + " " + args[4]
            print(dirConList[person])
    else:
        print("too many args")
        exit()
    
