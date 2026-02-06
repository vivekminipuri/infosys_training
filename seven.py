def addnum(a,b):
    return a+b
#add
print("addition")
a,b=map(int,input().split())
print("addition is",addnum(a,b))


#maximum of two nums
print("\nmaximum")
def maximum(a,b):
    if(a>=b):
        return a
    return b
a,b=map(int,input().split())
print("maximum is", maximum(a,b))



#factorial
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
print("\nfactorial")
n=int(input("Enter number:"))
print("Factorial",fact(n))


#prime
def prime(n):
    if(n<=1):
        return False
    if(n<=3):
        return True
    if((n%2)==0) or ((n%3)==0):
        return False
    i=5
    while(i*i<n):
        if((n%i)==0) or ((n%(i+2))==0):
            return False
        i+=6
    return True
print("\nPrime")
num=int(input("Enter number:"))
print("Prime result is",prime(num))


#calculator
def calculator(op):
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    def mul(n1,n2):
        return n1*n2
    def div(n1,n2):
        return n1/n2 if n2!=0 else "not possible"
    def rem(n1,n2):
        return n1%n2 if n2!=0 else "not possible"
    
    if(op=="+"):
        print(add(int(input("n1:")),int(input("n2:"))))
    if(op=="-"):
        print(sub(int(input("n1:")),int(input("n2:"))))
    if(op=="*"):
        print(mul(int(input("n1:")),int(input("n2:"))))
    if(op=="/"):
        print(div(int(input("n1:")),int(input("n2:"))))
    if(op=="%"):
        print(rem(int(input("n1:")),int(input("n2:"))))

print("\ncalculator")
while(True):
    op=input("Enter operator:  or end")
    calculator(op)
    if(op=="end"):
        break
       