import re

test_string = 'helloHELLO- 123_'

# pattern = re.compile(r'[ho]')
# pattern = re.compile(r'[12]')
# pattern = re.compile(r'[a-z]')
# pattern = re.compile(r'[0-9]')
# pattern = re.compile(r'[-]')
pattern = re.compile(r'[a-zA-Z0-9]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    
# A set is a set of characters inside a pair of square brackets [] with a special meaning. Append multiple conditions back-to back, e.g. [aA-Z].
# A ^ (caret) inside a set negates the expression.
# A - (dash) in a set specifies a range if it is in between, otherwise the dash itself.

# Examples:
# - [arn] Returns a match where one of the specified characters (a, r, or n) are present
# - [a-n] Returns a match for any lower case character, alphabetically between a and n
# - [^arn] Returns a match for any character EXCEPT a, r, and n
# - [0123] Returns a match where any of the specified digits (0, 1, 2, or 3) are present
# - [0-9] Returns a match for any digit between 0 and 9
# - 0-5 Returns a match for any two-digit numbers from 00 and 59
# - [a-zA-Z] Returns a match for any character alphabetically between a and z, lower case OR upper case