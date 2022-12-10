file = open("venv/d9/text9.txt")

input = file.readlines()

instrDir = []
instrDist = []
uniqueCoords = []

startCoords = [0,0]
curHCoords = [0,0]
curTCoords = [0,0]

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


for i in range(len(instrDir)):

    print(instrDir[i])
    print(instrDist[i])
    for m in range(int(instrDist[i])):
        if instrDir[i] == "U":
            curHCoords[1] = curHCoords[1]+1
        elif instrDir[i] == "D":
            curHCoords[1] = curHCoords[1]-1
        elif instrDir[i] == "L":
            curHCoords[0] = curHCoords[0]-1
        elif instrDir[i] == "R":
            curHCoords[0] = curHCoords[0]+1
        
        if diagonalCheck(curHCoords,curTCoords):
            print("adj")
        elif adjCheck(curHCoords,curTCoords):
            print("adj")
        else:
            print("not adj")

            #UR
            if ((curTCoords[0]+1 == curHCoords[0]) and (curTCoords[1]-2 == curHCoords[1])) or ((curTCoords[0]+2 == curHCoords[0]) and (curTCoords[1]-1 == curHCoords[1])):
                curTCoords[0] += 1
                curTCoords[1] -= 1
            #UL
            elif ((curTCoords[0]-1 == curHCoords[0]) and (curTCoords[1]-2 == curHCoords[1])) or ((curTCoords[0]-2 == curHCoords[0]) and (curTCoords[1]-1 == curHCoords[1])):
                curTCoords[0] -= 1
                curTCoords[1] -= 1
            #DR
            elif ((curTCoords[0]+1 == curHCoords[0]) and (curTCoords[1]+2 == curHCoords[1])) or ((curTCoords[0]+2 == curHCoords[0]) and (curTCoords[1]+1 == curHCoords[1])):
                curTCoords[0] += 1
                curTCoords[1] += 1
            #DL
            elif ((curTCoords[0]-1 == curHCoords[0]) and (curTCoords[1]+2 == curHCoords[1])) or ((curTCoords[0]-2 == curHCoords[0]) and (curTCoords[1]+1 == curHCoords[1])):
                curTCoords[0] -= 1
                curTCoords[1] += 1
            #U
            elif ((curTCoords[1]-2 == curHCoords[1]) and (curTCoords[0]==curHCoords[0])):
                curTCoords[1] -= 1
            #D
            elif ((curTCoords[1]+2 == curHCoords[1]) and (curTCoords[0]==curHCoords[0])):
                curTCoords[1] += 1
            #L
            elif ((curTCoords[0]-2 == curHCoords[0]) and (curTCoords[1]==curHCoords[1])):
                curTCoords[0] -= 1
            #R
            elif ((curTCoords[0]+2 == curHCoords[0]) and (curTCoords[1]==curHCoords[1])):
                curTCoords[0] += 1
            else:
                print("oops")
            
        
        print("head " + str(curHCoords))
        print("tail " + str(curTCoords))
        uniqueCoords.append(str(curTCoords))
       

setUniCoords = set(uniqueCoords)

print(len(setUniCoords))
    


            