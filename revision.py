def trait(l):
    l = sorted(l)
    i = 0
    while i<len(l)-1:
        if l[i] == l[i+1]:
            del l[i]
            i-=1
        i+=1
    return l


print(trait([50,1,1.213,1,2,42,1.213,1.213,105,1.213,20,23,21,23,19,1.213,10]))