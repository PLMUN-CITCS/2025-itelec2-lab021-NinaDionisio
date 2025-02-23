user_input = input("Enter a non-negative integer: ")
number = int(user_input)

if number < 0:
    print("Oops! Please enter a valid non-negative integer.")
else:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is {factorial}.")