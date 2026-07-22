a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
print("1.add 2.sub 3.mul 4.div")
choice=int(input("enter the choice:"))
if choice==1:
    print("result:",a+b)
elif choice==2:
    print("result:",a-b)
elif choice==3:
    print("result:",a*b)
elif choice==4:
    print("result:",a/b)
else:
    print("invalid choice")