file = open("text.txt","r")

str = file.readlines()
currentCals = 0
recordCals = []

for line in cals:
   # print(line)
    if line.strip():
        print(line)
        currentCals += int(line)
    else:
        print("reset")
        #if currentCals > recordCals[0]:
         #   recordCals = currentCals
        recordCals.append(currentCals)

        currentCals = 0

recordCals.sort()



print(recordCals)