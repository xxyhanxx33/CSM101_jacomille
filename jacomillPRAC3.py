students = {"Ana": [90, 85, 82],
            "Kirk": [72, 73, 78],
            "Liza": [69, 71, 83]}

highest = 0
lowest = 100
namehighest = ""
namelowest = ""
tally = 0

for name, grade in students.items():
  average = sum(grade) / len(grade)
  print(name, *grade, "average:", round(average, 2))


  if average > highest:
    highest = average
    namehighest = name


  if average < lowest:
    lowest = average
    namelowest = name


  for g in grade:
    if g < 75:
      tally = tally + 1

print(f"\nStudent {namehighest} got the highest average: {round(highest, 2)}")
print(f"Student {namelowest} got the lowest average: {round(lowest, 2)}")
print(f"There are {tally} grades which are below 75.")


