# def ArrayPairSum(a_list, k):
#     cor = []
#     for i in a_list:
#         if type(i) != int:
#             return False
#         for j in a_list:
#             if i+j == k:
#                 a_list.pop(i)
#                 y = [i,j]
#                 cor.append(y)
#                 print(cor)
#     return cor

# print(ArrayPairSum([1,3,2,2], 4))

def pair_sum(arr, k):

    if len(arr)<2:
        return False

    #Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num, target)), max(num, target)))

    # return len(output)
    print( '\n'.join(map(str,list(output))))

print(pair_sum([1,3,2,2], 4))

        