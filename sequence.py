#This algorithm generates the first n numbers of a sequence
# the sequence is 1, 2, 3, 6, 11, 20, 37 ...
#to start with we will accept the length of the sequence as integers n
#next we will make a loop that loops n times.
#The loop wil add the last 3 outcomes together to create the next number

n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 0
n2 = 1 
n3 = 0
for i in range(n):
    summa = n1+n2+n3
    n1 = n2
    n2 = n3
    n3 = summa
    print(summa)
    
