import pickle #this is inbuild just import it

fruits=['apple','oranges','bananas']
x=7
y=3.14
nuts=['pecans','almond']
grades=[99,100,26,77,85]

with open('data.pkl','wb') as f: # you can add a path to where you want the file to be save. wb means write binary  
    pickle.dump(fruits,f)
    pickle.dump(x,f)
    pickle.dump(y,f)
    pickle.dump(nuts,f)
    pickle.dump(grades,f)
with open('data.pkl','rb') as f2: # rb means read binary
    a=pickle.load(f2)
    b=pickle.load(f2)
    c=pickle.load(f2)
    d=pickle.load(f2)
    e=pickle.load(f2)
print(a)
print(b)
print(c)
print(d)
print(e)