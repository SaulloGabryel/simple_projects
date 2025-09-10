def elementK(array, k): 
    array.sort(reverse=True) #reverse the array by decreasing order
    stored = array[:3] #shows only the three first elements of the array
    return stored 

print(elementK([1, 23, 12, 9, 30, 2, 50], 3))

