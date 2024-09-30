def ismatch(t,p,n,m):
    if m==0:
        return n==0
    if n==0:
        return all(char == '*' for char in p[:m])
    if t[n-1]==p[m-1] or p[m-1]=='?':
        return ismatch(t,p,n-1,m-1)
    if p[m-1]=='*':
        return ismatch(t,p,n,m-1) or ismatch(t,p,n-1,m)



def checkWildCard(t,p):
    return ismatch(t,p,len(t),len(p))

p='ba*a?'
t='baaabaaaaajdvab'
print("Yes" if checkWildCard(t,p) else "No")

