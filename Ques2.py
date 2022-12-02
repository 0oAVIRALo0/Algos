nodes = 0
edges = 0
adjlist = []

f = open("test.txt", "r")
for line in f:
    list1 = []
    line = line.split()

    if line[1] == 'Nodes:':
        nodes = int(line[2])
        edges = int(line[4])

        for i in range(nodes):
            adjlist.append([])

    elif line[0] != "#":
        node1 = int(line[0])
        node2 = int(line[1])
        adjlist[node1-1].append(node2-1)
        adjlist[node2-1].append(node1-1)


isvisited = [0] * nodes

def isCyclic(adjlist, u, parent):
    if isvisited[u] == 0:
        isvisited[u] = 1

    for i in adjlist[u]:
        if isvisited[i] == 0:
            if(isCyclic(adjlist, i, u)):
                return True

        elif parent != i:
            return True
    
    return False

cyclicCheck = isCyclic(adjlist, 0, -1)

if cyclicCheck:
    print("True")
else:
    print("False")