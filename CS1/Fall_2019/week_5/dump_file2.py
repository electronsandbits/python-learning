'# dump_file2.py
# CS 1 demo by THC to read each line of a file and dump it to the console.

in_file = open('states.txt', 'r')

for line in in_file:
    print(line, end = '')
    
in_file.close()
