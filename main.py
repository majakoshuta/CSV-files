
with open("name-list.csv") as nameListFile:
    splitFile = nameListFile.read().splitlines()

for item in splitFile:
    nameList = item.split(",")
    print("{0} is {1} and {2}.".format(nameList[0], nameList[1], nameList[2]))