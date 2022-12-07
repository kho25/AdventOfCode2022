file = open("venv/d6/text6.txt","r")

str1 = file.readline()

for i in range (len(str1)):
    tempList = str1[i : i+14]
    tempSet = set(tempList)

    if (len(tempSet)) == 14:
        print("first" + str(i+14))
        break

