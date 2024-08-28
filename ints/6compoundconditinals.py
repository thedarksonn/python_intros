# color = input('enter color: ')
# if(color=='red' or color == 'Red' or color =='RED'):
#     print('your color is red')
# if(color != 'red' and color != 'Red' and color!='RED'):
#     print('color is red')
    
    
    
# number=float(input('enter number: '))
# if(number>=5 and number <=10):
#     print('your number is between 5 and 10')
# if(number<5 or number>10):
#     print('your number is not between 5 and 10')
    
    
number=float(input('please input your number: '))
rem = number%2

if(number>0 and rem==0):
    print('you have an even positive number')
if(number>0 and rem==1):
    print('you have an odd positive number')
if(number<0 and rem==1):
    print('you have an even negative number')
if(number<0 and rem==1):
    print('you have an odd negative number')
if(number==0):
    print('your number is 0')