# inputs : Rent price , Electricity charges , food charges , person
rent = int(input("Enter your hostel/rent charges: "))
food = int(input ("Enter your total charges spend on food :"))
electricity = int(input("Enter your Electricity spend:"))
#charge_per_unit = int(input("Enter the charge per unit:"))
person = int(input("Enter the number person in room:"))
#traveling = int(input("Enter the traveling charges:"))

total = (rent + food + """traveling""" ( electricity* """charge_per_unit"""))//person

print("Each person will pay : ", total)
