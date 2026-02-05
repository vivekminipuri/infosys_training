#first 
print("Name: Vivek, age: 19")

#2
message="Hello"
print(message)
print()

#3
num=int(input("Enter number:"))
for i in range(num):
    for j in range(num):
        if(i==0 or i==num-1):
            print("*",end=" ")
        elif(j==0 or j==num-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

print()

#4
items=int(input("Enter no. of items:"))
price=int(input("Enter price of each:"))
print(f"Items are {items}\nprice of each items is {price}\nTotal price is {items*price}")