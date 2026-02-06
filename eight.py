#list elements
li=list(map(int,input("Enter elements:").split()))
print(*li)

#sum of all elements in list
print("Sum:")
li=list(map(int,input("Enter numbers: ").split()))
s=0
for i in li:
    s+=i
print("Sum is",s)

print("\nLargest smallest")
#largest, smallest
li=list(map(int,input().split()))
maxi,mini=li[0],li[0]
for i in li:
    if(i>maxi):
        maxi=i
    if(i<mini):
        mini=i
print("maxi is",maxi,"mini is",mini)

#remove duplicates
print("\nRemove duplicates")
li=list(map(int,input().split()))
unique=set(li)
li=list(unique)
print("unique elements:")
print(*li)

#To Do app
#0-to do    1-in progress    2-done
li=[[] for i in range(3)]
print("\n0-todo\n1-in progress\n2-done\n3-exit")
while(True):
    option=int(input("option:"))
    if(option==0):
        work=input("Enter task:").lower()
        if(work not in li[0]):
            li[0].append(work)
        else:
            print(work,"is already in todo")
    elif(option==1):
        work=input("Enter task:").lower()
        if(work in li[0]):
            li[0].remove(work)
            li[1].append(work)
        else:
            print("Work is not in todo")
    elif(option==2):
        work=input("Enter task:").lower()
        if(work in li[1]):
            li[1].remove(work)
            li[2].append(work)
        else:
            print("work is not in progress")
    else:
        break
    print(li)

