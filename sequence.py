n = int(input("Enter the length of the sequence: ")) # Do not change this line


# The next number in the sequence is the sum of the last 3 numbers. 
# for every n we need the set the next number = first + second + third
# then update every varible to be the last so first = next, second = first, third = second
# we need to start with second number as 1

first_number = 3
second_number = 2 
third_number = 1


next_number = first_number + second_number + third_number
print(third_number)
print(second_number)
print(first_number)


for num in range(n - 3):
    
    next_number = first_number + second_number + third_number

    third_number = second_number
    second_number = first_number
    first_number = next_number

    print(next_number)
