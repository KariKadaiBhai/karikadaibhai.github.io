number = int(input("Enter an integer: "))

number_str = str(number)
number_str_reverse = number_str[::-1]

if number_str == number_str_reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
