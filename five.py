#positive or negative
print("Positive or Negative")
num=int(input())
if(num>=0):
    print("Positive")
else:
    print("Negative")


#vote
print("\nVote eligibility")
age=int(input())
if(age<18):
    print("Not eligible")
else:
    print("Eligible")

#largest of 2
print("\nLargest of 2 numbers")
a,b=map(int,input().split())
if(a==b):
    print("Both are equal")
elif(a>b):
    print(a,"is largest")
else:
    print(b,"is largest")

#grading
print("\nGrading")
marks=float(input())
if(marks>=90):
    print("A+")
elif(marks<90 and marks>=80):
    print("A")
elif(marks<80 and marks>=65):
    print("B")
elif(marks<65 and marks>=35):
    print("C")
else:
    print("Fail")

print("\nElectricity Bill")
#electricity using slabs
units=float(input("Enter no. of units: "))
if(units<=100):
    cost=units*1.5
elif(units<=200):
    cost=(100*1.5)+(units-100)*2.5
elif(units<=300):
    cost=(100*1.5)+(100*2.5)+(units-200)*3.5
else:
    cost=(100*1.5)+(100*2.5)+(100*3.5)+(units-300)*6
print("Total cost is",cost)

