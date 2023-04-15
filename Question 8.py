#program to calculate the average grade in 3 subs of a student
#take input from user for reg. no. and marks in three subjects
reg_no = int(input("Enter your registration no.: "))
M1 = int(input("Enter marks in first subject: "))
M2 = int(input("Enter marks in second subject: "))
M3 = int(input("Enter marks in third subject: "))
 
#adding marks in all subs and storing them in 'marks'
marks = M1 + M2 + M3
 
#calculating the average grade and storing them in 'avg'
avg = marks/3
 
#displaying the individual and average grade 
print("Marks' details for student, registration no.:", reg_no)
print("Marks in first subject:", M1)
print("Marks in second subject:", M2)
print("Marks in third subject:", M3)
print("Average grade in three subjects:", avg)
 
# End of the program.
