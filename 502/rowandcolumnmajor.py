def shape(array):
    for i in range(len(array)):
        print(' '.join(str(array[i])))
    print("\n")
    return "Array Dimensional Shape"

def row_major_order(array):
    base_address = array[0][0]
    c = len(array[0])
    for i in range(len(array)):
        for j in range(len(array[i])):
            address = base_address + 2*(c* i + j)
            print("The Address of ["+ str(i) +"] ["+ str(j) +"] -> " + str(address))

    print("\n")
    return "Row Major Order is completed"
        
def column_major_order(array):
    base_address = array[0][0]
    c = len(array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            address = base_address + 2*(c* i + j)
            print("The Address of ["+ str(i) +"] ["+ str(j) +"] -> " + str(address))
    
    print("\n")
    return "Column Major Order is completed"


array = [[1,2,3,10],[4,5,6,11],[7,8,9,12],[7,8,9,12]]

print(shape(array))
print("\n *********************************************")

print(row_major_order(array))
print("\n *********************************************")

print(column_major_order(array))
print("\n *********************************************")