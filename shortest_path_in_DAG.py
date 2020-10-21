from collections import deque , defaultdict
def kahn(g,n):
    indegree=[0]*n
    d=deque([])
    for i in range(n):
        for j in g[i]:
            indegree[j]+=1
        if(indegree[i]==0):
            d.append(i)
    c=0
    l=[]
    while(d):
        x=d.popleft()
        l.append(x)
        #print(x) u will get topological sort
        c+=1
        for i in g[x]:
            indegree[i]-=1
            if(indegree[i]==0):
                d.append(i)
    return l
def dag(g,n,source,w):
    x=[10**9]*n
    x[source]=0
    l=kahn(g,n)
    print(l)
    for i in l:
        for j in g[i]:
            if(x[j]>x[i]+w[(i,j)]):
                x[j]=x[i]+w[(i,j)]
    print(x)
d=defaultdict(list)
w=defaultdict(lambda x: 0)
for i in range(9):
    u,v,w1=list(map(int,input().split()))
    d[u].append(v)
    w[(u,v)]=w1
print(d,w)
dag(d,6,1,w)
