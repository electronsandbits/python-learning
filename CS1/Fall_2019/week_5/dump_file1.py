# dump_file1.py
# CS 1 demo by THC to read each line of a file and dump it to the console.
# But it puts an extra line in the output after each line.

in_file = open('states.txt', 'r')

for line in in_file:
    print(line)
    
in_file.close()
