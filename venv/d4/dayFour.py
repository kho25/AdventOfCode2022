file = open("venv/d4/text4.txt","r")

input = file.readlines()
overlap = 0

for line in input:
    num1 = int(line[0 : line.find("-")])
    num2 = int(line[line.find("-")+1 : line.find(",")])
    num3 = int(line[line.find(",")+1 : line.find("-",line.find(","))])
    num4 = int(line[line.find("-",line.find(","))+1 : len(line)])
    
    if (num1>=num3 and num2<=num4)|(num1<=num3 and num2>=num4):
        overlap += 1
    elif(num1>=num3 and num1<=num4)|(num2>=num3 and num2<=num4):
        overlap += 1

print(overlap)