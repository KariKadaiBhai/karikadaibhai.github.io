def count_char(s, c):
    if len(s) == 0:
        return 0

    if s[0] == c:
        return 1 + count_char(s[1:], c)

    return count_char(s[1:], c)


s = input("Enter a string: ")
c = input("Enter a character: ")
print("The number of occurrences of", c, "in", s, "is:", count_char(s, c))
