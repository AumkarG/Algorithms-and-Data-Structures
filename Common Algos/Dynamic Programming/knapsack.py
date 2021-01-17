n=int(input())
m=int(input())
w=[int(i) for i in input().split()]
p=[int(i) for i in input().split()]

table=[]
for i in range(n+1):
    table.append([0]*(m+1))

for k in range(w[0],m+1):
    table[1][k]=p[0]

for i in range(1,n):
    weight=w[i]
    profit=p[i]
    for j in range(1,m+1):
        if j<weight:
            table[i+1][j]=table[i][j]
        else:
            table[i+1][j]=max(table[i][j],table[i][j-weight]+profit)
for i in table:
    print(i)
print(table[n][m])