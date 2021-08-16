import re 

test_string = '123abc456789abc123ABC'

pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)

# findall()
# for match in matches:
#     print(match)
    
# Finds the first match or pattern
# match, search()
# print(matches)


### Methods on a match object

# start, end, span
# for match in matches:
#     print(match.span(), match.start(), match.end())
    
#group
for match in matches:
    print(match.group())