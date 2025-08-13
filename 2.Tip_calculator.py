print("Welcome to the Tip Calculator!")
print("What was the total bill? $", end="")
total_bill = float(input())
print("What percentage tip would you like to give? (10, 12, or 15) ", end="")
tip_percentage = int(input())
print("How many people to split the bill? ", end="")
num_people = int(input())
tip_amount = (tip_percentage / 100) * total_bill
total_amount = total_bill + tip_amount  
per_person = total_amount / num_people
print(f"Total bill: ${total_bill:.2f}")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount to be paid: ${total_amount:.2f}")
print(f"Each person should pay: ${per_person:.2f}")
print("Thank you for using the Tip Calculator!")
print("Have a great day!")
print("Please remember to tip your server!")
print("Goodbye!")