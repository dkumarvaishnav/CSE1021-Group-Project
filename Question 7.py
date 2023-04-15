#start of the program
# Take input for the base and height of the triangle 
P = float(input("Enter the principal amount: "))
I = float(input("Enter the annual interest rate: "))
N = int(input("Enter the number of years: "))
 
# Calculate the amount
T = P * (1 + I/100)**N
 
# Display the area of the triangle 
print("The amount of money after {} years is: {:.2f}".format(N, T))
 
#end of the program
