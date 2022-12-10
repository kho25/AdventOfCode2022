file = open("venv/d9/text9.txt")

input = file.readlines()

instrDir = []
instrDist = []
uniqueCoords = []

startCoords = [0,0]
curHCoords = [0,0]
curTCoords = [0,0]

#rope is 0-9 with 0 as head and 9 as tail
ropeCoords = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] 

nextUL = False
nextUR = False
nextDL = False
nextDR = False


for line in input:
    instrDir.append(line.split()[0])
    instrDist.append(line.split()[1])

print(instrDist)

def diagonalCheck(headCoord, tailCoord):
    if headCoord[0] == tailCoord[0]+1 and(headCoord[1]-1 == tailCoord[1] or headCoord[1]+1 == tailCoord):
        return True
    elif headCoord[0] == tailCoord[0]-1 and(headCoord[1]-1 == tailCoord[1] or headCoord[1]+1 == tailCoord):
        return True
    else:
        return False

def adjCheck(headCoord, tailCoord):
    if headCoord == tailCoord:
        return True
    if headCoord[0] == tailCoord[0]:
        if headCoord[1]-1 == tailCoord[1]:
            return True
        elif headCoord[1]+1 == tailCoord[1]:
            return True
        else:
            return False
    elif headCoord[1] == tailCoord[1]:
        if headCoord[0]-1 == tailCoord[0]:
            return True
        elif headCoord[0]+1 == tailCoord[0]:
            return True
        else:
            return False
    else:
        return False

print(startCoords)
print(adjCheck(startCoords, startCoords))

def moveNextPiece (backPos, frontCoord, backCoord):


    if diagonalCheck(frontCoord,backCoord):
        print("adj")
    elif adjCheck(frontCoord,backCoord):
        print("adj")
    else:
        print("not adj")

        #UR
        if ((backCoord[0]+1 == frontCoord[0]) and (backCoord[1]-2 == frontCoord[1])) or ((backCoord[0]+2 == frontCoord[0]) and (backCoord[1]-1 == frontCoord[1])) or (backCoord[0]+2 == frontCoord[0]) and (backCoord[1]-2 == frontCoord[1]):
            backCoord[0] += 1
            backCoord[1] -= 1
        #UL
        elif ((backCoord[0]-1 == frontCoord[0]) and (backCoord[1]-2 == frontCoord[1])) or ((backCoord[0]-2 == frontCoord[0]) and (backCoord[1]-1 == frontCoord[1])) or (backCoord[0]-2 == frontCoord[0]) and (backCoord[1]-2 == frontCoord[1]):
            backCoord[0] -= 1
            backCoord[1] -= 1
        #DR
        elif ((backCoord[0]+1 == frontCoord[0]) and (backCoord[1]+2 == frontCoord[1])) or ((backCoord[0]+2 == frontCoord[0]) and (backCoord[1]+1 == frontCoord[1])) or (backCoord[0]+2 == frontCoord[0]) and (backCoord[1]+2 == frontCoord[1]):
            backCoord[0] += 1
            backCoord[1] += 1
        #DL
        elif ((backCoord[0]-1 == frontCoord[0]) and (backCoord[1]+2 == frontCoord[1])) or ((backCoord[0]-2 == frontCoord[0]) and (backCoord[1]+1 == frontCoord[1])) or (backCoord[0]-2 == frontCoord[0]) and (backCoord[1]+2 == frontCoord[1]):
            backCoord[0] -= 1
            backCoord[1] += 1
        #U
        elif ((frontCoord[1]+2 == backCoord[1]) and (frontCoord[0]==backCoord[0])):
            backCoord[1] -= 1
        #D
        elif ((frontCoord[1]-2 == backCoord[1]) and (frontCoord[0]==backCoord[0])):
            backCoord[1] += 1
        #L
        elif ((frontCoord[0]+2 == backCoord[0]) and (frontCoord[1]==backCoord[1])):
            backCoord[0] -= 1
        #R
        elif ((frontCoord[0]-2 == backCoord[0]) and (frontCoord[1]==backCoord[1])):
            backCoord[0] += 1
        else:
            print("oops")

    return backCoord
        

for i in range(len(instrDir)):

    for m in range(int(instrDist[i])):
        if instrDir[i] == "U":
            ropeCoords[0][1] = ropeCoords[0][1]+1
        elif instrDir[i] == "D":
            ropeCoords[0][1] = ropeCoords[0][1]-1
        elif instrDir[i] == "L":
            ropeCoords[0][0] = ropeCoords[0][0]-1
        elif instrDir[i] == "R":
            ropeCoords[0][0] = ropeCoords[0][0]+1

        for j in range(len(ropeCoords)-1):
            
            ropeCoords[j+1] = moveNextPiece(j+1, ropeCoords[j],ropeCoords[j+1])
            if j+1 == 9:
                uniqueCoords.append(str(ropeCoords[9]))

        

setUniCoords = set(uniqueCoords)

print(setUniCoords)
print("unique coords: " + str(len(setUniCoords)))
    


            