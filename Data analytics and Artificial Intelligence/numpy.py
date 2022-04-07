import numpy as np

#Generate two NumPy arrays so that first array has integers from 10 to 40 (inclusive). Second array should have integers from 220 to 250 (inclusive). 
#Sum these arrays and present the result array.
a = np.arange(start=10, stop=41)
b = np.arange(start=220, stop=251)
c = np.add(a,b)

#Generate two-dimensional array with 10 rows and 7 columns containing integers starting from 100.
yksi = np.arange(start=100, stop=170)
kaksi = yksi.reshape(10,7)

#Generate three-dimensional array (3x3x3) with random floats
np.random.uniform(0,4, size=(3,3,3))

#Generate two one-dimensional arrays having integers between 1-50. First array should have even and second array should have odd numbers. 
#Finally multiply each element from corresponding index positions from these two arrays for the result array. For example [(1 x 2),(3 x 4),(5 x 6),(7 x 8)...]
even = np.arange(2,51,2)
odd = np.arange(1,51,2)
result = np.multiply(even,odd)

#Generate two-dimensional array (40 rows, 5 columns) containing random integers between 1 and 1000. 
#Filter the result array so that only numbers divisable with numbers 2 and 5 are presented (number must be divisable with both)
x = np.random.randint(1,1000, size=(40,5))
result = np.where((x % 10 == 0))
