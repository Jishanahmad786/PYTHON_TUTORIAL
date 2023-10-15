sum=1
sum2=0
n=int(input("Enter n number"))
while(n>0):
  r=n%10
  if(r%2==0):
    sum=sum*r
  else:
    sum2=sum2+r
  n=n//10
print(sum)
print(sum2)
