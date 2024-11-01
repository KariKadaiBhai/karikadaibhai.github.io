number = int(input("Enter an integer: "))
biggest = smallest = number % 10

while number > 0:
    digit = number % 10
    if digit > biggest:
        biggest = digit
    elif digit < smallest:
        smallest = digit
    number //= 10

print("The biggest digit is", biggest)
print("The smallest digit is", smallest)
