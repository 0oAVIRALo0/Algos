nodes = 0
edges = 0
adjlist = []

f = open("test.txt", "r")
for line in f:
    list1 = []
    line = line.split()

    if (line[1] == 'Nodes:'):
        nodes = int(line[2])
        edges = int(line[4])

        for i in range(nodes):
            adjlist.append([])

    elif line[0] != "#":
        node1 = int(line[0])
        node2 = int(line[1])
        adjlist[node1-1].append(node2-1)
        adjlist[node2-1].append(node1-1)

print(adjlist)
# u = starting node
isVisited = [0] * nodes
path = ""

def hamiltonianCheck(isVisited):
    for i in range(0,len(isVisited)):
        if isVisited[i] == 0:
            return False
    return True

flag = False
def hamiltonian(adjlist, u, isVisited, org):
    global flag
    if isVisited[u] == 0:
        isVisited[u] = 1
    
    for i in adjlist[u]:
        if i == org:
            if (hamiltonianCheck(isVisited)):
                flag = True
                return
            else:
                continue

        elif isVisited[i] == 0:
            hamiltonian(adjlist, i, isVisited, org)
            
    isVisited[u] = 0

a = hamiltonian(adjlist, 0, isVisited, 0)
print(flag)
