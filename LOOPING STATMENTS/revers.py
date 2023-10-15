rev=0
n=int(input("Enter n number"))
while(n>0):
  r=n%10
  rev=rev*10+r
  n=n//10
print(rev)
  
