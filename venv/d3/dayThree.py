file = open("venv/d3/text3.txt","r")

input = file.readlines()

sum = 0

myArr = []

for line in input:
    print(line)
    myArr.append(line)


for i in range(len(myArr)//3):

    s1 = set(myArr[i*3])
    s2 = set(myArr[i*3+1])
    s3 = set(myArr[i*3+2])

    s1.remove("\n")
    s2.remove("\n")
    #s3.remove("\n")
    
    print("Hello")
    print(myArr[i*3])
    print(s1)


    letter = s1.intersection(s2.intersection(s3))
    print(letter)
    strletter = str(letter)[2:3]

    if ord(strletter) < 96:
        sum += ord(strletter)-64+26
    else:
        sum += ord(strletter)-96


print(sum)