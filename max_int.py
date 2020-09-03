# Algorithm
# This algorithm will find the maximum positive input by a user
# First we will ask for an input, afther that, we will compare 
# that input to the last input, if it is higher, we will change
# the max_int variable to that number.
# if the input is negative, we will stop
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0 
# Fill in the missing code
while num_int >= 0:
    if num_int > max_int:
        max_int = num_int
    print("The maximum is", max_int)    # Do not change this line
    num_int = int(input("Input a number: "))