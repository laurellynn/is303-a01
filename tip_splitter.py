'''
Laurel Lynn
IS 303 - A01

Tip Splitter Calculator
This program calculates how much each person should pay when splitting a tip

Inputs: 
- Restaurant name (string)
- Bill amount (float)
- Tip percentage (float)
- number of people splitting bill (int)

Processes: 
- convert bill amount, tip percentage, and number of people to numbers
- calculate total with tip: bill * (1 + tip percent/100)
- calculate amount per person: total with tip / number of people

Outputs:
- Print restaurant name, bill amount, tip percentage, number of people, and amount per person in a formatted message
'''

restaurant_name = input("What is the name of the restaurant?")
bill_amount = float(input("What is the bill amount?"))
tip_percentage = float(input("What percentage tip do you want to leave?"))
number_of_people = int(input("How many people will be splitting the bill?"))


total_with_tip = bill_amount * (1 + tip_percentage / 100)
amount_per_person = total_with_tip / number_of_people

print("---")
print(f"{restaurant_name} | bill amount: ${bill_amount:.2f} | tip percentage: {tip_percentage:.2f}% | number of people: {number_of_people}")
print(f"Total with tip: ${total_with_tip:.2f} | Amount per person: ${amount_per_person:.2f} ")
