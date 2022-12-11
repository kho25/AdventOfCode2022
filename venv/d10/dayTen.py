file = open("venv/d10/text10.txt")

input = [x for x in open("venv/d10/text10.txt").read().strip().split('\n')]

xValue = 1
cycleNumber = 1

specificXValues = []
answerArr = []

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

for i in range(len(input)):
    
    if input[i] == "noop":
        print("noop")
        cycleNumber += 1
        
    else:
        print(str(input[i][5:]))
        cycleNumber +=1
        checkCycleNum()
        cycleNumber +=1
        xValue += int(input[i][5:])

    checkCycleNum()
  

print(specificXValues)
print(answerArr)
print(sum(answerArr))

    