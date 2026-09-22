marks3 = float(input("Enter marks for Subject 3: "))


marks4 = float(input("Enter marks for Subject 4: "))
marks1 = float(input("Enter marks for Subject 1: "))
marks5 = float(input("Enter marks for Subject 5: "))
marks2 = float(input("Enter marks for Subject 2: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total / 5

print("Marks:", marks1, marks2, marks3, marks4, marks5)
print("Total Marks:", total)
print("Average Marks:", percentage)

if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 50:
    print("Result: pass")
else:
    print("Result: fail")