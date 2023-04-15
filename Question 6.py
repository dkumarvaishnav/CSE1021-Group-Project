#program to find simple interest
#function to accept 3 parameters P, R and T
 
def simple_interest(P,T,R):
 
    #calculating the simple interest
    SI = (P * T * R)/100
 
    #displaying the simple interest as output
    print('The Simple Interest is', SI)
        
#taking inputs from user
P = int(input("Enter the principal amount :"))
T = int(input("Enter the time period :"))
R = int(input("Enter the rate of interest :"))
 
#calling the function with user inputs as arguments
simple_interest(P,T,R)
 
# End of the program.
