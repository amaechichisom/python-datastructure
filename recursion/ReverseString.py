# def reverse(n, output = []):
#     if len(n) == 0:
#         return ''.join(output)
#     else:
#         n = list(n)
#         output.append(n.pop())
#         return reverse(n)

# print(reverse('hello'))

# def reverse(s):

#     #Base Case
#     if len(s) <= 1:
#         return s

#     #Recursion
#     return reverse(s[1:]) + s[0]

# print(reverse('hello'))