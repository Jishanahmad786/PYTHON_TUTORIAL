sum=0
n=int(input("Enter n number"))
orig=n
while(n>0):
  r=n%10
  sum=sum+r**3
  n=n//10
if(orig==sum):
  print("Armstrong")
else:
  print("Not Armstrong")
  
