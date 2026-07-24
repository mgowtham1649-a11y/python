print("welcome to the tip calculator")
bill=float(input("what was the total bill$:"))
tip=int(input("how much you like to tip the waiter$:"))
people=int(input("how  many persons split the bill:"))
tip_as_percentage=tip/100
total_tip_amount=bill+tip_as_percentage
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"each persons to pay:${final_amount}")
