# -*- coding: utf-8 -*-

# Input#
#N = int(input())
n, m = map(int, input().split())

a=[]
b=[]
for i in range(m):
    a_in,b_in = map(int, input().split())
    a.append(a_in)
    b.append(b_in)



k = int(input())
c=[]
d=[]
for i in range(k):
    c_in,d_in = map(int, input().split())
    c.append(c_in)
    d.append(d_in)



def calc(tar):
    global a,b,c,d
    ans = 0
    assigned = []
    for i in range(k):
        if not tar & (1<<i):
            assigned.append(c[i])
        else:
            assigned.append(d[i])

    for i in range(m):
        if a[i] in assigned and b[i] in assigned:
            ans += 1
    
    return ans



ans =0

for i in range(2**k):
    ans = max(ans,calc(i))

print("{}".format(ans))

