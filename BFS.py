import collections

def bfs(graph, root):
    seen, queue = set([root]), collections.deque([root])
    while queue:
        vertex = queue.popleft()
        print(vertex,end=" ")
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)


# create the graph in adjacency list representation
#adjLists = [[1, 3, 4],[2,5,6],[],[],[],[],[]]


adjLists=[]

#User Input Code for creating adjLists for the Graph

#No of vertices
n=int(input("Enter the no of vertices"))

for i in range(n):
    l=[]
    #no of edges from current vertex
    print("Enter no of directed Edges from vertex ",i)
    edges=int(input())

    for j in range(edges):
        #target vertex
        print("Enter the target vertex of ",j+1," edge.")
        target=int(input())
        l.append(target)
              
              
    adjLists.append(l)
#print(adjLists)

#Start vertex for dfs   
start=int(input("Enter the start vertex for BFS"))

print("The BFS is:-")

bfs(adjLists,start)
