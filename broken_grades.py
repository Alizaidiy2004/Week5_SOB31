# Calculating Grades (ok, let me think about this one)
change  have been made
# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) # SHA added "int" with "("

exam_three = str(input("Input exam grade three: ")) # SHA changed variable name "exam_3" to "exam_three" and str()n to int()

grades = [exam_one, exam_two, exam_three] # SHA added missing commas
sum_grades = 0 # SHA changed varialbes name 'sum' t o"sum_grades" avoiding built-in function
for grade in grades: # SHA fixed 'grade' to "grades"
  sum_grades += grade # SHA changed sum operation into short way

avg = round(sum_grades / len(grdes))  # SHA fixed misspelled variable 'grade' to 'grades'
                                      # & added 'round' function to round the average

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90 # SHA added missing colon(:)
    letter_grade = "B"
elif avg >=70 and avg < 80: # SHA fixed 'avg> 69 ' to ' avg >=70'
    letter_grade = "C"      # SHA fixed quote error ("C') to ("C")
elif avg >= 60 and avg< 70: # SHA fixed range 'avg<=69' to 'avg>=60' and 'avg >= 65' to 'avg<70'
    letter_grade = "D"
else:                        # SHA  changed 'elif:' to 'else:' for final condition
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg)) # SHA made to outside loop i.e. to print once

print("Grade: " + letter_grade)

if letter-grade is "F":        # SHA changes 'letter-grade is "F"' to letter_grade == "F"'
    print("Student is failing.") # SHA added parentheses() for print
else:
    print("Student is passing.") # SHA added parentheses() for print

  # Edited by Syed Hasnain Ali

