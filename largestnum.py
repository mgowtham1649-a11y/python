a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>=b and b>=c):
  print("largest number is:",a)
elif(b>a and b>c):
  print("largest number is:",b)
else:
  print("largest number is:",c)
  
