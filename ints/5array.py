## what is an array in python
# is basicly a data structure which can hold morethan value at the same time

# python list and array have thesame way of storing data. but the difference is that an array can store only single data types value but list can have or store any type of data
# to create an array in python you have to import the array modules. there are three ways you can import the array the array modules
# - import array  (without alias)
# - import array as ar (using alias)
# - from array import * (using*)

import array

a=array.array('i',[1,2,3]) #.array is the array constructure then the 'i' is the type code representing int saying what data type that array will hold
print(a)

## so if you import array using alias: import array as ar
# a=ar.array('1',[1,2,3])
#print(a)

## so if you import array using: from array import *
# a=array('1',[1,2,3])
#print(a)

## accesing array elements. the same as list


