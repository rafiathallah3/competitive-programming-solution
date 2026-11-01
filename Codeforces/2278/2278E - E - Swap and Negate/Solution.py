t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int, input().split()))
    a=sum(l)
    o=sorted(l[0::2])
    e=sorted(l[1::2])
    m=n//2
    for i in range(m):
        if((o[i]+e[i])<0):
            a=a-2*(o[i]+e[i])
    print(a)