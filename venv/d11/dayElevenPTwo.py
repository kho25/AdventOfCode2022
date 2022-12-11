input = [x for x in open("venv/d11/text11.txt").read().strip().split('\n')]

class baseMonk(object):
    def __init__(self, mNum, items, opType, opNum, test, tMonk, fMonk, inspections):
        self.mNum = mNum
        self.items = items
        self.opType = opType
        self.opNum = opNum
        self.test = test
        self.tMonk = tMonk
        self.fMonk = fMonk
        self.inspections = inspections
    def testPrint(self):
        print(self.mNum)

monkeys = []

def makeMonk(num):
    print("Monke num: " + str(num))

    currentInput = input[num*7:num*7+7]

    #items
    itemsList = currentInput[1][currentInput[1].find(": ")+2:]
    items = itemsList.split(", ")
    print(items)
    
    #opType
    opType = currentInput[2][currentInput[2].find("old ")+4:currentInput[2].find("old ")+5]
    print(opType)

    #opNum 
    opNum = currentInput[2][currentInput[2].find("old ")+6:]
    print(opNum)

    #test
    test = currentInput[3][currentInput[3].find("by ")+3:]
    print(test)

    #fMonk
    tMonk = currentInput[4][currentInput[4].find("y ")+2:]
    print(tMonk)

    #tMonk
    fMonk = currentInput[5][currentInput[5].find("y ")+2:]
    print(fMonk)

    moke = baseMonk(num,items,opType,opNum,test,tMonk,fMonk,0)

    return moke

def printItems():
    for i in range(len(monkeys)):
        print("Monkey " + str(i) + " items: " + str(monkeys[i].items))

#make monkeys
for i in range(8):
    monkeys.append(makeMonk(i))

divMulti = 1
for i in range(len(monkeys)):
  divMulti *= int(monkeys[i].test)

  
#run 20 rounds
for rounds in range(10000):
    for i in range(len(monkeys)):
        #printItems()
        for j in range(len(monkeys[i].items)):
            #print("opNum " + str(monkeys[i].opNum))
            worryLv = monkeys[i].items[j]
            worryLv = int(worryLv)
            #print("worryLV " + str(worryLv))


            #change worry lv
            if monkeys[i].opType == "+":
                worryLv += int(monkeys[i].opNum)
            elif monkeys[i].opType == "-":
                worryLv -= int(monkeys[i].opNum)
            elif monkeys[i].opType == "*":
                if monkeys[i].opNum == "old":
                    worryLv *= worryLv
                else:
                    worryLv *= int(monkeys[i].opNum)
            elif monkeys[i].opType == "/":
                worryLv /= int(monkeys[i].opNum)


            #change worry lv divide testnums

            worryLv = worryLv % divMulti
            tf = worryLv % int(monkeys[i].test)

            #move the item

            if tf == 0:
                #print("To true monk: " + str(monkeys[i].tMonk))
                monkeys[int(monkeys[i].tMonk)].items.append(worryLv)
            else:
                #print ("To false monk: " + str(monkeys[i].fMonk))
                monkeys[int(monkeys[i].fMonk)].items.append(worryLv)

            #increment turns
            monkeys[i].inspections +=1
        
        monkeys[i].items.clear()


        
#printItems()

inspectionTimes = []
for i in range(len(monkeys)):
    print("Monkey " + str(i) + " inspected " + str(monkeys[i].inspections) + " items")
    inspectionTimes.append(monkeys[i].inspections)

inspectionTimes.sort()
print(inspectionTimes)
