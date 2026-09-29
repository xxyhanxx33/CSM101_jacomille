students = {}

number = int(input("Enter number of students: "))

for i in range(number):
  print(f"\nStudent {i + 1}")

  name = input("Enter Student Name: ")

  grade1 = float(input("Enter grade 1: "))
  grade2 = float(input("Enter grade 2: "))
  grade3 = float(input("Enter grade 3: "))

  students[name] = (grade1, grade2, grade3)

print("\n====== STUDENT RECORDS =====")

for name, grades in students.items():
  average = sum(grades) / len(grades)
  print(name, *grades, "Average:", round(average, 2))


highest = 0
lowest = 100
namehighest = ""
namelowest = ""
tally = 0

for name, grade in students.items():

  average = sum(grade) / len(grade)


  if average > highest:
    highest = average
    namehighest = name


  if average < lowest:
    lowest = average
    namelowest = name


  for g in grade:
    if g < 75:
      tally += 1

print(f"\nStudent {namehighest} got the highest average: {round(highest, 2)}")
print(f"Student {namelowest} got the lowest average: {round(lowest, 2)}")
print(f"There are {tally} grades which are below 75.")


