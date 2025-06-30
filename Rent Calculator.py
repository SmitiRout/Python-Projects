## Inputs we need from the user
# Total rent
# Total amount of food ordered
# electricity units spend
# Charge per unit
# Persons living in tha flat

# Output
# Total amount to per person to be paid

rent = int(input("Enter your flat rent="))
food = int(input("Enter the amount of food ordered ="))
electricity_spend = int (input ("Enter the total electricity spend = "))
per_unit_charge = int (input ("Enter the amount charge per unit = "))
persons = int(input("Enter the number of persons living in flat = "))

total_electrcity_bill = electricity_spend * per_unit_charge


output = (rent + food + total_electrcity_bill) // persons
 
print ("Enter each person has to pay " , output ) 