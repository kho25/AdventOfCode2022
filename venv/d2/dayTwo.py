file = open("venv/d2/text2.txt","r")

input = file.readlines()
score = 0

for line in input:
    c1 = line.split()[0]
    c2 = line.split()[1]

    #rock
    if c1 == "A": #Rock
        if c2 == "X":
            score += 0+3 
        elif c2 == "Y": 
            score += 3+1
        elif c2 == "Z":
            score += 6+2
    elif c1 == "B": #Paper
        if c2 == "X":
            score += 0+1
        elif c2 == "Y":
            score += 3+2
        elif c2 == "Z":
            score += 6+3
    elif c1 == "C": #Scissors
        if c2 == "X":
            score += 0+2
        elif c2 == "Y":
            score += 3+3
        elif c2 == "Z":
            score += 6+1
    
print(score)

