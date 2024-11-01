s = input("Enter a string: ")
c = input("Enter a character: ")
count = 0

for char in s:
    if char == c:
        count += 1

print("The number of occurrences of", c, "in", s, "is:", count)
