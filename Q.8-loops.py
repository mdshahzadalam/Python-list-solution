#8. Write a python script to calculate sum of digits of a given number

n=int(input("Enter a number:-"))
sum=0
for i in range(1,n+1):
      rem=n%10
      n=n//10
      sum+=rem

print(sum)