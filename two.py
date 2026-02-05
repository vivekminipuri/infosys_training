#1
integer=int(input("enter integer:"))
floatvar=float(input("enter float number:"))
boolvar=bool(input("enter True or False:"))
stringvar=input("Enter a string:")

print("Integer is",integer)
print("Float is",floatvar)
print("boolean is",boolvar)
print("string is",stringvar)

#5 datatypes
print("Datatypes")
print(f"datatype of {integer} is",type(integer))
print(f"datatype of {floatvar} is",type(floatvar))
print(f"datatype of {boolvar} is",type(boolvar))
print(f"datatype of {stringvar} is",type(stringvar))


#2
a,b=map(int,input("Enter two numbers a b:").split())
print(f"before swap a:{a},b:{b}")
a=a+b
b=a-b
a=a-b
print(f"after swap a:{a}, b:{b}")

#3
a,b=map(int,input("enter two numbers").split())
a,b=int(a),int(b)
s=a+b
print("sum is:", s)

#4
p=float(input("Enter principal amount:"))
t=int(input("Enter time in years:"))
r=float(input("Enter Rate of interest:"))
SI=(p*t*r)/100
print("Simple interest is:",SI)

