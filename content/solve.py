from collections import Counter
# find top k
def solve(li,k):
    import heapq
    new_k = Counter(li)

    xy=heapq.nlargest(k,new_k.keys(),key=new_k.get)
    return xy
def solve(li,k):
    import myheapq
    new_k = Counter(li)
    new_k = new_k.values

    xy=myheapq.nlargest(k,)
    return xy
print(solve([1,1,2,9,8,6,9,5,6,2],3))
