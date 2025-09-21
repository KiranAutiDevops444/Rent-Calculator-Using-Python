##Input we need from the user
#totel Rent
#Totel food ordered for snacking
#Electricity units spend
#Charge per unit
#persons living in room/flat
##Output
#Total Amount you have to pay is

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter amount of food ordered = "))
electricity_spend = int(input("Enter the totel of electicity spend ="))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of persons living in room/flat ="))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ",output)