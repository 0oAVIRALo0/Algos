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

# u = starting node
isvisited = [0] * nodes
path = ""

def hamiltonian(adjlist, u, isvisited, org):
    if (len(isvisited) == len(adjlist) - 1):
        flag = 0
        for i in adjlist[u]:
            if (i == org):
                flag = 1
                break
        
        if (flag == 1):
            print("True")
        else:
            print("False")


    isvisited[u] = 1

    for i in adjlist[u]:
        if isvisited[i] == 0:
            hamiltonian(adjlist, i, isvisited, org)
    
    isvisited[u] = 0

hamiltonian(adjlist, 0, isvisited, 0)
