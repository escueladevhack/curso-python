def power_of_two(number):
    # Just validating types
    if not isinstance(number, int):
        return "", False
    if number < 0:
        return "", False
    # Transform the number to binary
    binary_number = bin(number)
    # Remove the prefix
    binary_number = binary_number[2:]
    # If the first binary is a 1 and the rest are 0, is a power of two
    if binary_number[0] == "1" and int(binary_number[1:]) == 0:
        return len(binary_number) - 1, True
    return "", False

print(power_of_two(""))

def especial_reverse(string):
    # Just validating types
    if not isinstance(string, str):
        return ""
    # Import regular expression
    import re
    # Compile an expression for all non letters
    reg_exp = re.compile("\W")
    # Find all groups of non-letters
    all_non_letters = re.finditer(reg_exp, string)
    # Remove all non letters
    all_letters = list(re.sub(reg_exp, "", string))
    # Reverse the list
    all_letters.reverse()
    # Re insert all the groups in the current index
    [all_letters.insert(x.start(), x.group()) for x in all_non_letters]
    # Re-transform to string
    return "".join(all_letters)

print(especial_reverse("a,b$c"))