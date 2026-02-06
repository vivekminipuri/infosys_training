#1 to n
print("1 to n")
n=int(input("Enter number:"))
for i in range(1,n+1):
    print(i,end=" ")
print("\n")

#even from 1 to 150
print("1 to 150")
for i in range(2,150+1,2):
    print(i,end=" ")
print("\n")

#factorial
print("Factorial")
n=int(input("Enter number:"))
f=1
for i in range(1,n+1):
    f*=i
print(f)


print("\nReverse")
#reverse number
n=int(input("num:"))
s=0
while(n>0):
    rem=n%10
    s=(s*10)+rem
    n=n//10
print("Reversed number is: ",s)

#palindrome
print("\nPalindrome")
n=int(input())
temp=n
s=0
while(n>0):
    rem=n%10
    s=(s*10)+rem
    n=n//10
if(temp==s):
    print(temp,"is palindrome")
else:
    print(temp,"is not palindrome")
    
    
