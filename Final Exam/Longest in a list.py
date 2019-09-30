def longestRun(L):
    k=0
    n=1
    i =[]
    while (k+n) <= (len(L)-1):
        if L[k+n] >= L[k+n-1]:
            n+=1
        else:
            i.append(n)
            n=1
            k+=1
    i.append(n)
    return max(i)