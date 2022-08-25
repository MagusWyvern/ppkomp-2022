sequence = input()
nterms = int(input())

sequence = list(sequence.split())

def change_to_int(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def change_to_str(lst):
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    return lst

change_to_int(sequence)

difference = sequence[1] - sequence[0]

for n in range(0, nterms):
    new_number = sequence[-1] + difference
    sequence.append(new_number)

change_to_str(sequence)
    
def list_to_string(list):
    return ' '.join(list)

print(list_to_string(sequence))