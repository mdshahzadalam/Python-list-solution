#2. Write a python script to calculate sum of squares of first N natural numbers
n=int(input("Enter a number:-"))
sum=0
for e in range(1,n+1):
    sum=sum+e*e
print(sum)