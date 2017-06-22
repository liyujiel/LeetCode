# Python zip

zip function 

take iliterate object to parameter, and put them as tuple.
return with list

i.e.

>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)

[(1,4),(2,5),(3,6)]

>>> zip(a,c)

[(1,4),(2,5),(3,6)]

zip(*zipped)
[(1,2,3),(4,5,6)]