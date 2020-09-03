
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

# Ef num int er stærri heldur en seinasta tala þá geymum við hana.
# Þegar num int er ekki negative þá hættum við að spurja um input og prentum stærstu töluna.
max_int = 0
while num_int > 0:
    if num_int > max_int:
        max_int = num_int

    num_int = int(input("Input a number: "))

print("The maximum is", max_int)    # Do not change this line
