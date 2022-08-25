"""
Aisyah Humairah had completed her final examinations.

Given the number of subjects and a list of subjects with mark obtained by Aisyah Humairah.
You are to determine the best subject that Aisyah Humairah has obtained.
"""


num_subjects = int(input())
percentages_subjects = {}
for n in range(0, num_subjects):
    subject_name, mark = input().split(", ")
    achieved, full = mark.split("/")
    percentage = round( ( int(achieved) / int(full) ) * 100, 2 )
    percentages_subjects.update({subject_name: percentage})

# print(percentages_subjects)

def find_highest(dict):
    highest = 0
    for key, value in dict.items():
        if value > highest:
            highest = value
            highest_subject = key
    return highest_subject

print(find_highest(percentages_subjects))