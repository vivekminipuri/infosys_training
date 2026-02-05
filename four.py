#arithmetic
a,b=map(int,input("Enter a b: ").split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a/b)
print(a%b)

#odd even
num=int(input("Enter number:"))
if((num%2)==0):
    print("Even")
else:
    print("Odd")

#greater
a,b=map(int,input("Enter a,b: ").split())
if(a>b):
    print(a)
else:
    print(b)

#inrange
val1,val2=map(int,input("Enter two numbers val1,val2: ").split())
num=int(input("Enter number:"))
if(num in range(val1,val2+1)):
    print("Present")
else:
    print("Not present")


#calculator
while(True):
    c=input("Enter operator: or type end to stop")
    if(c=="end"):
        break
    match(c):
        case '+':
            n1,n2=map(int,input().split())
            print(n1+n2)
        case '-':
            n1,n2=map(int,input().split())
            print(n1-n2)            
        case '*':
            n1,n2=map(int,input().split())
            print(n1*n2)    
        case '/':
            n1,n2=map(int,input().split())
            print(n1/n2)    
        case '%':
            n1,n2=map(int,input().split())
            print(n1%n2)    
        case default:
            print("invalid")
            