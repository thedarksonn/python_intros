# file handeling
# to write to a file in python we use a funtion call open.
# this function requires 2 parameters. the first parameter is the filename
# and the second parameter is the mode of the file

# the mode is of three types 
# - reading 'r'
# - writing 'w'
# - append 'a'

## writing to a file
# open ('log.txt', 'w')
# we can assign the open file to a variable  so that each time you want to access that file you use the variable
f = open ('log.txt', 'w')
f.write("writing to the text file")
f.close()

## reading a file

f = open ('log.txt', 'r')
filedata = f.read()
print(filedata)
f.close()

## appending to a file (adding data to the file)
f = open ('log.txt', 'a')
f.write("new writing")
f.close()