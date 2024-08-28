## collections in python
# there are four collections data types in python which are used to store collections of data.
# and also there is a collection modules in python. this mudule is build in you don't have to install it. you just import it 
## this are basically container data types namely;   lists, tuples,sets and dictionary
# list declear in []
# tuple ()
# set {}
# dictoionry {}

## 1 nametuple

from collections import namedtuple

a = namedtuple('courses', 'name, technology')
s = a('data scienec','python')
print(s)

# you will see something like this as result : courses(name='data scienec', technology='python')

## 2 deque

## 3 chainmap
from collections import ChainMap
a={1:'education',2:'python'}
b={3:'ml',4:'ai'}

a1 =ChainMap(a,b)

print(a1)

# ChainMap({1: 'education', 2: 'python'}, {3: 'ml', 4: 'ai'}) it wil joint both dictionary as one

## 4 counter

from collections import Counter
a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
c = Counter(a)
print (c)
# Counter({2: 5, 4: 3, 1: 2, 3: 2, 5: 2, 6: 1}) 
## 5 orderdict
## 6 defaualtdict
## 7 userdick, userlist,userstring

