JacomilleName = input("Enter employee name: ")
JacomillePosition = input("Enter job position: ")
JacomilleHoursWorked = float(input("Enter actual hours worked: "))
JacomilleMonthlySalary = 0
match JacomillePosition.lower():
    case "janitor":
        JacomilleMonthlySalary = 18000

    case "clerk":
        JacomilleMonthlySalary = 22000

    case "cashier":
        JacomilleMonthlySalary = 24000

    case "manager":
        JacomilleMonthlySalary = 40000

    case _:
        print("Invalid job position.")
        exit()

JacomilleBasicHalfMonth = JacomilleMonthlySalary / 2
JacomilleHourlyRate = JacomilleBasicHalfMonth / 88

JacomilleAbsentHours = 0
JacomilleAbsenceDeduction = 0
JacomilleOvertimeHours = 0
JacomilleOvertimeRate = 0
JacomilleOvertimePay = 0


if JacomilleHoursWorked < 88:

    JacomilleAbsentHours = 88 - JacomilleHoursWorked
    JacomilleAbsenceDeduction = JacomilleAbsentHours * JacomilleHourlyRate


elif JacomilleHoursWorked > 88:

    JacomilleOvertimeHours = JacomilleHoursWorked - 88
    JacomilleOvertimeRate = JacomilleHourlyRate * 1.25
    JacomilleOvertimePay = JacomilleOvertimeHours * JacomilleOvertimeRate

else:

    JacomilleAbsentHours = 0
    JacomilleOvertimeHours = 0



JacomilleNetSalary = JacomilleBasicHalfMonth - JacomilleAbsenceDeduction + JacomilleOvertimePay


print("\n==========================================")
print("        SET A - STANDARD PAYROLL")
print("==========================================")

print(f"Employee Name       : {JacomilleName}")
print(f"Job Position        : {JacomillePosition}")
print(f"Actual Hours Worked : {JacomilleHoursWorked:.2f}")

print("\n----------- SALARY COMPONENTS -----------")
print(f"Monthly Salary      : \033[32m₱{JacomilleMonthlySalary:,.2f}\033[0m")
print(f"Basic Half-Month    : ₱{JacomilleBasicHalfMonth:,.2f}")
print(f"Hourly Rate         : ₱{JacomilleHourlyRate:,.2f}")

print("--------------- ABSENCE ----------------")
print(f"Absent Hours        : {JacomilleAbsentHours:.2f}")
print(f"Absence Deduction   : ₱{JacomilleAbsenceDeduction:,.2f}")

print("\n-------------- OVERTIME ----------------")
print(f"Overtime Hours      : {JacomilleOvertimeHours:.2f}")
print(f"Overtime Rate       : ₱{JacomilleOvertimeRate:,.2f}")
print(f"Overtime Pay        : ₱{JacomilleOvertimePay:,.2f}")

print("\n==========================================")
print(f"NET HALF-MONTH SALARY: ₱{JacomilleNetSalary:,.2f}")
print("==========================================")