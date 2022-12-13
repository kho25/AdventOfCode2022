file = open("venv/d12/text12.txt")

input = file.read().splitlines()

elevations = []

#-13 is S
#-27 is E

start = None
end = None

for line in input:
    b = [*line]
    row = [ord(i)-96 for i in b]
    elevations.append(row)


for i in range(len(elevations)):
    for j in range (len(elevations[0])):
        if elevations[i][j] == -13:
            elevations[i][j] = 1
            start = (i, j)
        elif elevations[i][j] == -27:
            elevations[i][j] = 26
            end = (i, j)

#returns all possible locations to move to
def nextLoc(row, col):
    locations = []
    #left
    if col>0 and elevations[row][col] + 1 >= elevations[row][col-1]:
        #can move left 
        locations.append((row,col-1))
    #right
    if col<len(elevations[0])-1 and elevations[row][col] + 1 >= elevations[row][col+1]:
        #can move right 
        locations.append((row,col+1))
    #up
    if row>0 and elevations[row][col] + 1 >= elevations[row-1][col]:
        #can move up 
        locations.append((row-1,col))
    #down
    if row<len(elevations)-1 and elevations[row][col] + 1 >= elevations[row+1][col]:
        #can move down 
        locations.append((row+1,col))

    return locations


coordList = [start]

parent = {start:None} 

while len(coordList) != 0:
    currentLoc = coordList.pop(0)

    if currentLoc == end:
        break 

    neighbors = nextLoc(currentLoc[0],currentLoc[1])

    for i in range(len(neighbors)):
        if neighbors[i] not in parent:
            coordList.append(neighbors[i])
            parent[neighbors[i]] = currentLoc


counter = 0
currentParentLoc = end

while start != currentParentLoc:
    counter += 1

    currentParentLoc = parent[currentParentLoc]


print("Shortest dist: " + str(counter))


    





    






