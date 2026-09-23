first_number = int(input("Enter the first number: \n"))
second_number = int(input("Enter the second number: \n"))

result = first_number * second_number

print(f"{first_number} * {second_number} = {result}")

if result < 0:
    print("The result is negative.\n")
elif result == 0:
    print("The result is positive and negative.\n")
else:
    print("The result is positive.\n")
