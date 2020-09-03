n = int(input("Enter the length of the sequence: ")) # Do not change this line

# The next number in the sequence is the sum of the last 3 numbers.
# We find the first n number of numbers in the sequence.
first_number = 0
second_number = 1 
third_number = 0

next_number = 0
for num in range(n):
    
    #fyrsta talan er þá = first_number(1) + second_number(0) + third_number(0) = 1

    #then the first number has to be = next number and so on
    next_number = first_number + second_number + third_number

    third_number = second_number
    second_number = first_number
    first_number = next_number

    print(next_number)




