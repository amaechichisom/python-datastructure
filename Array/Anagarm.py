import sys

# def anagram(s1, s2):
#     s1 = s1.replace(' ','').lower()
#     s2 = s2.replace(' ','').lower()

#     if(sorted(s1) == sorted(s2)): return True
#     else: return False

def anagram2(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge Case Check
    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
            
    for k in count:
        if count[k] != 0:
            return False
    
    return True

print(anagram2('god', 'dog'))
print()