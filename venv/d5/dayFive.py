# NOT FINISHED
cargoF = open("venv/d5/cargo.txt","r")

input = cargoF.readlines()

cargoStack = []

for line in cargoF:
    #print()
    for i in range(3):
        print(cargoF[i*3, i*3+1])
        if cargoF[i*4+1, i*4+2] != " ":
            cargoStack[i].append(cargoF[i*4+1, i*4+2])

print(cargoStack)
