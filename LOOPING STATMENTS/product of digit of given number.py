sum=1
n=int(input("Enter n number"))
while(n>0):
  r=n%10
  sum=sum*r
  n=n//10
print(sum)
