array = [
    [1,2,3,10],
    [4,5,6,11],
    [7,8,9,12], 
    [14,15,13,12]
    ]
print("************************ The array dimensions: *********************************")   
print(array)
print("*******************************************************************************")

base_address = array[0][0]


# column_major_order\
print("\n********************************Column Major order: ******************************** \n")
print("*******************************************************************************")

c = len(array)
for i in range(len(array)):
    for j in range(len(array[i])):
        address = base_address + 2*(c* i + j)
        print("The Address of ["+ str(i) +"] ["+ str(j) +"] -> " + str(address))

print("\n")

#row_major_order
print("*******************************************************************************")
print("\n******************************** Row Major order: ********************************\n")
print("*******************************************************************************")

c = len(array[0])
for i in range(len(array)):
    for j in range(len(array[i])):
        address = base_address + 2*(c* i + j)
        print("The Address of ["+ str(i) +"] ["+ str(j) +"] -> " + str(address))

print("\n")