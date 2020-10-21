def dfs_iterative(adjLists, s):
    stack = []
    stack.append(s)
    n = len(adjLists)
    visited = []
    for i in range(0,n):
        visited.append(False)
         
    while(len(stack)>0):
        v = stack.pop()
        if(not visited[v]):
            visited[v] = True
            print(v, " ", end='')
 
            # auxiliary stack to visit neighbors in the order they appear
            # in the adjacency list
            stack_aux = []
            for w in adjLists[v]:
                if(not visited[w]):
                    stack_aux.append(w)
            while(len(stack_aux)>0):
                stack.append(stack_aux.pop())
                     
 
# ------------------------------------------------------------------
 
# create the graph in adjacency list representation
#adjLists = [ [1,2,3], [5,6], [4], [2,4], [1], [], [4]]

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
start=int(input("Enter the start vertex for DFS"))
print("The DFS is:-")

dfs_iterative(adjLists,start)
