# import sys

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


isVisited1 = [0] * nodes

def DFS(neighbours, u):
    if isVisited1[u] == 0:
        isVisited1[u] = 1
    
    for i in neighbours[u]:
        if isVisited1[i] == 0:
            DFS(neighbours, i)

DFS(adjlist, 0)

def DFSCheck():
    for i in isVisited1:
        if i == 1:
            return True

    return False

b = DFSCheck()

if b:
    print("True")
else:
    print("False")
