from itertools import count
import json
import os
clear = lambda: os.system('cls')
file = open("students.json")
data = json.load(file)



countf = 0
countm = 0
totf = 0
totm = 0
totgf = 0
totgm = 0


for student in data["Students"]:
    if student["Gender"] == "Female":
        totgf += int(student["Grade"])
        countf += 1
        totf += int(student["Age"])
    else:
        totgm += int(student["Grade"])
        countm += 1
        totm + int(student["Age"])


print({countf, countm})
print({totf, totm})
print({totgm, totgf})

#print(f"20 and below: {avg20/count20}\nBetween 20 and 30: {avg2030/count2030}\n30 and More: {avg30/count30}")

