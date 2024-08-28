# when ever we use the open function it alocates some memory in the system for the file and when
# we use close, we releses the memory.is always good practices to always close a file when you open it
# when we use the with keyword it, it releases the memory automatically.

# the three lines of code we wrote in the 11files.py to open,append and close a file can be written as this

with open('log.txt','a') as f:
    f.write('\n new content')
