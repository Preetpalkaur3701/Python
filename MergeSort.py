def Merge(l1, l2):
    l3=[]
    while(len(l1)>0 and len(l2)>0):
        if (l1[0]<l2[0]):
            l3.append(l1.pop(0))
        else:
            l3.append(l2.pop(0))
    while(len(l1)>0):
        l3.append(l1.pop(0))
    while(len(l2)>0):
        l3.append(l2.pop(0))
    return l3

def MergeSortRec(lis,start,end):
    length=end-start+1
    if(length==1):
        return [lis[start]]
    if(length==2):
        if(lis[start]<lis[end]):
            return [lis[start],lis[end]]
        else:
            return[lis[end],lis[start]]
    mid= (start+end)//2
    l1 = MergeSortRec(lis,start,mid)
    l2 = MergeSortRec(lis,mid+1,end)
    return Merge(l1,l2)
def MergeSort(lis):
    return MergeSortRec(l1,0,len(lis)-1)


