# cook your dish here
T=int(input())
for i in range(T):
    n,k,start,mine=[int(i) for i in input().split()]
    k=k%n
    if(start==mine):
        print("YES")
    else:
        if(k==0):
            print('NO')
        else:
            if(n%k!=0):
                print('YES')
            else:
                    x=(start+k)%n
                    flag=0
                    while(x!=start):
                        if x==mine:
                            print('YES')
                            flag=1
                            break
                        else:
                            x=(x+k)%n
                    if(flag==0):
                        print('NO')