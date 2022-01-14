'# read_file.py
# CS 1 demo by THC.
# Shows various ways to read a file.

# Read the entire file into a single string.
in_file = open('states.txt', 'r')
text = in_file.read()
print('Result of in_file.read():')
print(text)
in_file.close()

# Read the entire file into a single list, where each
# line in the file becomes one newline-terminated
# string in the list.
in_file = open('states.txt', 'r')
text = in_file.readlines()
print('Result of in_file.readlines():')
print(text)
in_file.close()

# Read the first line of the file one character at a time.
in_file = open('states.txt', 'r')
print('\nResult of in_file.read(1) until reading a newline:')
char = ''
while char != '\n':
    char = in_file.read(1)
    print(char)
print('DONE!')
in_file.close()

# Read the file 16 characters at time.
in_file = open('states.txt', 'r')
print('\nResult of in_file.read(16) until getting to the end of the file:')
while True:
    chars = in_file.read(16)
    if len(chars) > 0:
        print(chars)
    else:
        break
print('DONE!')
in_file.close()