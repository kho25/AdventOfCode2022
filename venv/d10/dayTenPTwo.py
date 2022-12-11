file = open("venv/d10/text10.txt")

input = [x for x in open("venv/d10/text10.txt").read().strip().split('\n')]

xValue = 1
cycleNumber = 0

specificXValues = []
answerArr = []

visualArr = ["","","","","","",""]
spritePos = [-1,0,1]

def checkCycleNum():
    if cycleNumber == 20:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)
    elif cycleNumber == 60:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)
    elif cycleNumber == 100:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)
    elif cycleNumber == 140:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)
    elif cycleNumber == 180:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)
    elif cycleNumber == 220:
        specificXValues.append(xValue)
        answerArr.append(xValue*cycleNumber)

def incSpritePos():
    spritePos[0] += 1
    spritePos[1] += 1
    spritePos[2] += 1

def spriteDraw():

    print("spritePos mod: " + str(spritePos[2]%40))
    if (spritePos[2]%40 == xValue) or (spritePos[1]%40 == xValue) or (spritePos[0]%40 == xValue):
        print("Spritepos: " + str(spritePos))
        print("cycle num: " + str((cycleNumber)//40))
        visualArr[(cycleNumber)//40] = visualArr[(cycleNumber)//40] + "##"
       
    else:
        print("cycle num: " + str((cycleNumber-1)//40))
        visualArr[(cycleNumber)//40] = visualArr[(cycleNumber)//40] + ".."


for i in range(len(input)):
    print(input[i])
    if i == 0:
        print("xValue: " + str(xValue))
        spriteDraw()
        checkCycleNum()
        incSpritePos()

    for j in range(6):  
        print(visualArr[j])

    if input[i] == "noop":
        cycleNumber += 1

        
    else:
        cycleNumber +=1
        print("xValue: " + str(xValue))
        spriteDraw()
        checkCycleNum()
        incSpritePos()
        for j in range(6):  
            print(visualArr[j])
        cycleNumber +=1
        xValue += int(input[i][5:])

    print("xValue: " + str(xValue))
    spriteDraw()
    checkCycleNum()
    incSpritePos()
    

for i in range(6):  
    print(visualArr[i])
    