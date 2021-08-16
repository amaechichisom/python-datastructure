# def MissingElement(a_list, b_list):
#     if len(a_list)<2:
#         return False

#     c = sorted(a_list)
#     d = sorted(b_list)

#     for i in range(len(c)):
#         # print(str(c[i]) +" ->"  + str(d[i]))
#         try:
#             if c[i] != d[i]:
#                 return c[i]
#         except IndexError:
#             return c[i]
#     print("No Missing Number")
        

# print(MissingElement([1,2,3,4,5,6,7], [1,2,3,4,5,6,7]))

#Sample Solution 1

# def finder(arr1, arr2):
#     arr1.sort()
#     arr2.sort()

#     for num1, num2 in zip(arr1, arr2):
#         if num1 != num2:
#             return num1

#     return arr[-1]

#SAMPLE SOLUTION 2

# import collections

# def finder2(arr1, arr2):

#     d = collections.defaultdict(int)

#     for num in arr2:
#         d[num] += 1
    
#     for num in arr1:
#         if d[num] == 0:
#             return num
        
#         else:
#             d[num] -=1

# print(finder2([1,2,3,4,5,6,7], [1,2,3,4,6,7]))
    
#SAMPLE SOLUTION 3

# def finder3(arr1,arr2):
#     result = 0

#     #Perform an XOR between the numbers in the arrays
#     for num in arr1+arr2:
#         result^=num
#         print(result)

#     return result

# print(finder3([1,2,3,4,5,6,7], [1,2,3,4,6,7])) 
