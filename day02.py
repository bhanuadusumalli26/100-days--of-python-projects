print("Welcome to the tip calculator!")
#to take bill amount
bill = float(input("What was the total bill? $"))
#to enter tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#members
people = int(input("How many people to split the bill?"))
#tip in percentage
tip_as_percent = tip / 100
#total tip amount i.e tip amount is added based on bill
total_tip_amount = bill * tip_as_percent
#total bill amount
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#for readable format taking two decimal points
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
