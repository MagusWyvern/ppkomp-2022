"""
Aisyah Humairah and Aina Tasnim went back to their hometown during Hari Raya Aidilfitri. It was a heavy traffic journey. To keep themselves occupied and avoiding them from getting bored, both of them compete in a competition of totaling up digits of vehicle plate numbers that they found.
The winner is based on who gets to find the most vehicle plate number that:
1. total of the digits is an odd number, and
2. all the digits of the plate number are odd digits

Given a list of vehicle plate number, you are to display the digit sum of it.
For digit sum that is an odd number, replace that digit sum with the string 'S1'.
For vehicle plate number that are all odd digits, display the string 'S2'.
For digit sum that is an odd number and the vehicle plate number are all odd digits, display the string 'S1S2'.
"""

nterms = int(input())

vehicle_plates = {}

for n in range(0, nterms):
    plate = input()
    # only add the numbers in the plate, not the letters
    numbers = [int(x) for x in plate if x.isdigit()]

    # print(numbers)

    # add up all the numbers in the list
    total = sum(numbers)

    # check if the total is an odd number and all the numbers in the list are odd
    if total % 2 != 0 and all(x % 2 != 0 for x in numbers):
        vehicle_plates.update({plate: "S1S2"})

    # check if all the numbers in the list are odd
    elif all(x % 2 != 0 for x in numbers):
        vehicle_plates.update({plate: "S2"})
    

    # check if the total is an odd number
    elif total % 2 != 0:
        vehicle_plates.update({plate: "S1"})
    

    # if the sum is even, add the sum to the dictionary
    elif total % 2 == 0:
        vehicle_plates.update({plate: total})

# print all the valus in the dict
for key, value in vehicle_plates.items():
    print(value)
    
