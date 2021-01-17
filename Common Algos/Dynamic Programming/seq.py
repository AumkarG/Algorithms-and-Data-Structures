s=input()
n=len(s)
lng=[1]*n
vowels=['a','e','i','o','u']
lst=[]
for i in s:
    if i in vowels:
        lst.append(i)
print(lst)
for i in range(len(lst)):
    for j in range(i):
        if(lst[i]>=lst[j]):
            lng[i]=max(lng[j]+1,lng[i])

print(max(lng))
