#6. Write a python script to calculate factorial of a given number

n=int(input("Enter a number:-"))
fact=1
if n<0:
    print("factorial does not exist....")
elif n==0:
    print("0")
for i in range(1,n+1):
    fact=fact*i
print(fact)