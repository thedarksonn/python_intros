# variables they are case sencitive
x = 1
y = 2
X = 5
Y = 4

print (x)
print (X)
print (y)
print (Y)


# data types
## numbers, string, list, dictionary, tuple, set, range

##### numbers data types

## interger
x = 10
# float
x = 10.234
## complex
p = 25j

# to check the type of a variable just use type(varaiblename)
print(type(p))

## bolean: bolean only returns true of false
num = 10 > 9
print (num)
# this will print true because 10 is greater than 9

##### strings data types

# you can write strings using single or double quotes. the index of a string starts at 0. in programing as a whole you start counting from 0
x = 'hello'
y = "world"
# g = input()

# check the len of a string use
print(len(y))

#  you can access a paticular index in a string.
print(y[2]) # this will print the second index at the string which is 'r' since w=0,o=1,r=2 and so on
print(y[2:5]) # it will print from 2 to 5 'rld'

##### list data types
# ordered, can be changed. duplicate entries are present
fruits = ['apple', 'kiwi','banana']
print (fruits)

boys = [10,20,30,'boys','girls']
print (boys)

# you can do thesame things you did above the strings here
boys[2] = 40 # this updates index2 to 40. so index 2 = 30 will be update now to 40
print(boys)

boys.append(19) # this will add the value 19 at the end of the list
print(boys)

boys.insert(4,100) # this will add 100 after the index value 4
print(boys)
# append adds at the end of the list. inserts adds where you want it to be added by spesifying the index number
# you can reverse the list using the reverse function
boys.reverse()
print (boys)

##### dictionary data types
# unordered, can be changed, no duplicate entries are present.  dictionaries deals with key value pares
animals = {'reptiles':'snake','mammals':'whale','amphibians':'frogs'}
print(animals)
print(animals['reptiles']) # this will print 'snake

programs = {1:'python', 2:'data science','third':'machine learning'}
programs['third']='loops' # it will update machine leanring to 'loops'
programs['four'] = 'mobile and ai' # it will add  four: mobile and ai
print(programs)

###### tuple
# ordered, cannot be changed. duplicate entries are present.
girls = ('lion','monkey',1,2,3,4)

