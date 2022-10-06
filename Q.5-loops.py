#5. Write a python script to calculate sum of first N even natural numbers

n=int(input("Enter a number:-"))
sum=0
for e in range(1,n+1):
   #if e%2==0:
      sum=sum+e*2
print(sum)