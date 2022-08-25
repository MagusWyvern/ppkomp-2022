"""
Given a list that has a base and number representation on that base, you have to find the sum of all numbers and give your answer in base 10.

There is at least 3 input lines.
Each line except the last one has integer a and b, each represent the base and number representation on that base.
The last line has a number -1 and no other line will have .
"""

# check if the input given is -1
# if it is, break the loop

base_with_numbers = {}
numbers_no_base = []

try:
    while True:
        base, number = input().split(" ")
        base = int(base)
        base_with_numbers.update({number: base})
except:
    pass

print(base_with_numbers)

# for every value in the dictionary, convert it to base 10

for key, value in base_with_numbers.items():

    # convert the value to base 10
    to_be_converted = str(to_be_converted)
    converted = int(key, to_be_converted)
    numbers_no_base.append(converted)

print(sum(numbers_no_base))