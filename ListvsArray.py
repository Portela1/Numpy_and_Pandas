import numpy as np

#Creating List / Array ######################
Python_list = [1,2,3]
Numpy_array = np.array([1,2,3])
print(Python_list)
print(Numpy_array)
print(" ")

# Apending elements ######################
Python_list.append(4)
###
# Not easily done for Numpy Array
###
print(Python_list)
print(Numpy_array)
print(" ")

# Sum of two Lists / Array ############################
Python_list2 = []
for a in Python_list:
    Python_list2.append(a+a)
Numpy_array = Numpy_array + Numpy_array
print(Python_list2)
print(Numpy_array)
print(" ")


# Mult of two lists / Array
Python_list3 = []
for a in Python_list:
    Python_list3.append(a*a)
Numpy_array = Numpy_array*Numpy_array
print(Python_list3)
print(Numpy_array)
print(" ")



##############################
## Very good numpy benefits ##
##############################
np.sqrt(Numpy_array)
np.log(Numpy_array)
np.exp(Numpy_array)
print(Numpy_array)




