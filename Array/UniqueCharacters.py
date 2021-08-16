# def uni_char(s):
#     return len(s) == len(set(s))

# print(uni_char("dferg"))

def uni_char2(s):
    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)
    return True