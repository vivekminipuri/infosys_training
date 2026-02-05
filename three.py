#1
name=input("Enter your name:")
print("Hello namaste",name)

#2 sum
a,b=map(int,input().split())
print("sum is",a+b)

#3 subjects
sub1,sub2,sub3=map(float,input("Enter three subject marks separated by space:").split())
print("Total marks are:",sub1+sub2+sub3)

#4 salary
sal=float(input("Enter your salary in lakhs:"))
print("Yearly salary is",sal*12, "lakhs")

#5 profile
name=input("enter name:")
age=int(input("enter age:"))
gender=input("Enter gender:")
education=input("Enter degree:")
print("User profile")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Education: {education}")

