# j=1
# while (j <= 10):
#     print (j)
#     j= j+1
# print("that's all")

# j=1.0
# while (j <= 10):
#     print (j)
#     j= j+.1
  
# print("that's all")

# j=1.0
# while (j <= 10):
#     print (j)
#     j= j+.1
#     j=round(j,1)
# print("that's all")

numgrades=int(input('how many grades do you have: '))
j=0
grades=[]
while (j<numgrades):
    grd=float(input('enter your grade: '))
    grades.append(grd)
    j=j+1
j=0
while (j<numgrades):
    print(grades[j])
    j=j+1