file = open("venv/d7/text7.txt","r")
input = file.readlines()

directNames = []
directSizes = []

currentDir = ""
currentDirNum =0

def iterate(tempDir, fileSize):
    directSizes[directNames.index(tempDir)] = directSizes[directNames.index(tempDir)] + fileSize
    print("DirectSizes: " + str(directSizes))
    print(tempDir)
    if tempDir == "/root":
        #directSizes[directNames.index(tempDir)] += directSizes[directNames.index(tempDir)] + fileSize
        return
    else:
        tempDir = tempDir[0:tempDir.rfind("/")]
        print("stucl")
        iterate(tempDir, fileSize)
        

for line in input:
    print(line)
   
    if line[0:6] == "$ cd /": #root direct
        directNames.append("/root")
        directSizes.append(0)
        currentDir = directNames[0]
        print(currentDir)

    elif line[0 : 7] == "$ cd ..": #back one direct
        print("Back a direct")
        currentDir = currentDir[0 : currentDir.rfind("/")] 
        currentDirNum = directNames.index(currentDir)
        print(currentDir)

    elif line[0:4] == "$ cd": #open new direct
        print("open direct")
        print(str(line[5:len(line)]))
        currentDir = currentDir + "/" + str(line[5:line.find("\n")])
        print(currentDir)
        currentDirNum = directNames.index(currentDir)
        print(directNames.index(currentDir))

    elif line[0:4] == "$ ls": #idk this is useless
        print("listing sub elements")

    elif line[0:3] == "dir": #directory is in parent direct
        directNames.append(currentDir + "/" + str(line[4:len(line)-1]))
        print(currentDir + "/" + str(line[4:len(line)-1]))
        print(directNames)
        directSizes.append(0)

    else: #this must be a file, read the file size and add to all parents
        #currentSize = directSizes[currentDirNum]
        print("adding file")
        #TODO iterate though all previous directs
        iterate(currentDir, int(line[0:line.find(" ")]))
       
        print(int(line[0:line.find(" ")]))
        print(directSizes) 

print(directNames)
print(directSizes)

sumNum = 0

totalDirectSize = 0

for i in range(len(directSizes)):
    if directSizes[i] <= 100000:
        sumNum += directSizes[i]
#ANSWER TO PT1
print("PT1 ans: " + str(sumNum))

directSizes.sort()

print(directSizes)
deletedDirSize = 0

for i in range(len(directSizes)):
    print(directSizes[len(directSizes)-1] - directSizes[i])
    if directSizes[len(directSizes)-1] - directSizes[i] <= 40000000:
        deletedDirSize = directSizes[i]
        break

#ANSWER TO PT2
print(deletedDirSize) 
