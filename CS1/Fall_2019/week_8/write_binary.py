out_file = open("output.txt", "wb")
out_file.write(bytes("abcdef", "UTF-8"))
out_file.write(bytearray("GHIJK\n", "UTF-8"))
out_file.write(bytearray("lmnop\n", "UTF-8"))
out_file.close()

in_file = open("output.txt", "rb")
first_line = in_file.readline()
print(first_line)
next_block = in_file.read(4)
print(next_block)
print(next_block.decode())
in_file.close()