import math
j=3
prime=[2]
counter=1
while(counter<100000):
    lim=int(math.sqrt(j))
    flag=0
    if(j%2!=0):
        for i in prime:
            if(i>lim):
                break
            else:
                if(j%i==0):
                    flag=1
                    break
        if(flag==0):
            prime.append(j)
            counter+=1
    j+=1
p=[1]
for i in prime:
    p.append(i)
print(prime)

