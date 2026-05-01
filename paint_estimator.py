'''
Laurel Lynn
IS 303 - A01

Paint Estimator
This program calculates how many fallons of paint are needed for a room 
based on the (height * width)/350
One gallon covering 350 sq ft.

Inputs:
- Room name (string)
- Wall height in ft (float)
- total wall width in ft (float)

Processes:
- convert height and width to numbers
- calculate gallons needed: (height * width)/350

Outputs:
- Print room name, gallons needed in a formatted message
'''

room_name = input("What is the room name?")
room_height = float(input("How tall is the room in feet?"))
room_width = float(input("What is the total width of the walls in feet?"))

total_sq_ft = room_height * room_width
gallons_needed = total_sq_ft / 350

print("---")
print(f"{room_name} | room  {room_height} ft | total wall width: {room_width} ft | gallons needed: {gallons_needed:.2f}")