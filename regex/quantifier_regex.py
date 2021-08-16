# * : 0 or more
# + : 1 or more
# ? : 0 or 1, used when a character can be optional
# {4} : exact number
# {4,6} : range numbers (min, max)

import re

test_string = 'hello_123'

pattern = re.compile(r'\d+')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
