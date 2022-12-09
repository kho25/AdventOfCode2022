file = open("venv/d8/text8.txt")

input = file.read().splitlines()

visable = 0
print(input)
lineNum = 0

myHeights = []

for line in input:
    b = [*line]
    row = [int(i) for i in b]
    myHeights.append(row)

rowLen = len(myHeights[0])

#PART 1
for row in range (len(myHeights)):
    print("row " + str(row) + "\n")
    for col in range (len(myHeights[0])):
        print("col " + str(col))
        #edge
        tempVertList = []

        for i in range(len(myHeights)):
            tempVertList.append(myHeights[i][col])

        print("tempList " + str(tempVertList))
        if row == 0 or col == 0 or row == (len(myHeights)-1) or col == (len(myHeights[0])-1):
            visable +=1
        else:
            #lefts
            vis = 0
            checked = False
            print("Tree height " + str(myHeights[row][col]))
            #left
            print("rMax: " + str(max(myHeights[row][col+1:])))
            if myHeights[row][col] > max(myHeights[row][:col]):
                visable += 1
                print("add Lvisable")
            #right
            elif myHeights[row][col] > max(myHeights[row][col+1:]):
                visable += 1
                print("add Rvisable")
            #top
            elif myHeights[row][col] > max(tempVertList[:row]):
                visable += 1
                print("add Tvisable")
            elif myHeights[row][col] > max(tempVertList[row+1:]):
                visable += 1
                print("add Bvisable")

def nextLTree(i, row, col):
    print("next height " + str(myHeights[row][col-i]))
    print("i: " + str(i))
    
    if col == i:
        print("stupid return1")
        return i

    elif (myHeights[row][col-i]) >= myHeights[row][col]:
        print("stupid return2")
        return i
    
    else:
        i += 1
        nextLTree(i, row, col)

def test(num):
    return num*2

senScores = []
#PART 2
for row in range (len(myHeights)):
    print("row " + str(row) + "\n")
    for col in range (len(myHeights[0])):
        print("col " + str(col))
        
        if row == 0 or col == 0 or row == (len(myHeights)-1) or col == (len(myHeights[0])-1):
            senScores.append(0)
            print("edge")
        else:
            tempVertList = []

            for i in range(len(myHeights)):
                tempVertList.append(myHeights[i][col])

            LSenScore = 1
            RSenScore = 1
            TSenScore = 1
            BSenScore = 1
            print(myHeights[row][:col+1])
            #left
            for i in range (len(myHeights[row][:col+1])-1):
                if(myHeights[row][col-LSenScore])>=myHeights[row][col]:
                    break
                elif LSenScore == col:
                    break
                else:
                    LSenScore+=1
            print(LSenScore)
            #right
            for i in range(len(myHeights[row][col+1:])-1):
                if(myHeights[row][col+RSenScore])>=myHeights[row][col]:
                    break
                elif RSenScore == len(myHeights[row][col+1:]):
                    break
                else:
                    RSenScore+=1
            print(RSenScore)
            #top
            for i in range(len(tempVertList[:row])):
                if(tempVertList[row-TSenScore])>=tempVertList[row]:
                    break
                elif TSenScore == len(tempVertList[:row]):
                    break
                else:
                    TSenScore+=1
            print(TSenScore)
            #bottom
            for i in range(len(tempVertList[row:])+1):
                if(tempVertList[row+BSenScore])>=tempVertList[row]:
                    break
                elif BSenScore == len(tempVertList[row:])-1:
                    break
                else:
                    BSenScore +=1
            print(BSenScore)

            senScores.append(LSenScore*RSenScore*BSenScore*TSenScore)

    
senScores.sort()

print("Part 2 Solution: " + str(senScores))    
print("Part 1 Solution: " + str(visable))       