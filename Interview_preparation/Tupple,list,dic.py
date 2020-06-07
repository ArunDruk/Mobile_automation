####################################################################################################
# # Converting Tuple to list and then appending value and then converting List back to Tuple.
####################################################################################################
# T=(1,2,3,4,5)
# L=list(T)
# L.append(77)
# print(type(L),L)
# T=tuple(L)
# print(type(T),T)

####################################################################################################
# Dictionary operations Add, remove, delete, Shallow copy operations.
####################################################################################################
D={1:'a',2:'b',3:'c'}
# print(D)
# D[5]='zz' # Adding a new element to the exisisting dictionary
# print(D)
#
# del D[3] # Removing the key and its value from the dictionary
# print(D)
#
# D.clear() # Removing all the elements from the dictionary
# print(D)
#
# del D # Deleting the dictionary
# print(D)
# print(D.get(4),"Key 4 is not present")
# D_copy=D.copy() # Shallow copy of dictionary.
# print(D_copy)

####################################################################################################
#Converting list of tuples to single list elements
####################################################################################################
list_of_tuple=[(1,11),(2,22),(3,33)]
L=[]
# for i in list_of_tuple:
#     for element in i:
#         L.append(element)
# print(L,type(L))

[L.append(element) for i in list_of_tuple for element in i] # Using list comprehension.
print(L,type(L))