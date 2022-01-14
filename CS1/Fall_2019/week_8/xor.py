# xor example for CS 1 lecture
# Original version by Devin Balkcom
# Major changes by THC

# Return the string representation of a binary number with
# at least a certain number of bits.
def binary_rep(x, bits):
    bin_rep = bin(x)[2:]    # remove "0b"
    if len(bin_rep) >= bits:
        return bin_rep
    else:
        return ("0" * (bits - len(bin_rep))) + bin_rep

# Print a nicely formatted example of XORing two ints.
def print_xor_example(a, b):
    num_bits = max(len(bin(a)), len(bin(b))) - 2    # -2 because of "0b"

    print("")
    print("     " + binary_rep(a, num_bits) + " (" + str(a) + ")")
    print(" xor " + binary_rep(b, num_bits) + " (" + str(b) + ")")
    print("  =  " + binary_rep(a ^ b, num_bits) + " (" + str(a ^ b) + ")")

print("0 xor 0 is " + str(0 ^ 0))
print("0 xor 1 is " + str(0 ^ 1))
print("1 xor 0 is " + str(1 ^ 0))
print("1 xor 1 is " + str(1 ^ 1))

print_xor_example(0b001000, 0b001001)
print_xor_example(7, 42)
print_xor_example(7, 42 ^ 42)
print_xor_example(7, 7 ^ 42)
print("")

# Make an XOR key that is a bytearray 4 bytes long.
key_length = 4

# First way: Allocate and initialize the entire bytearray in one operation.
xor_key = bytearray([1, 2, 3, 4])

# Second way: Allocate the entire bytearray and fill it in one byte at a time.
# xor_key = bytearray(key_length)
# for i in range(key_length):
#     xor_key[i] = i + 1

# Third way: Start with an empty bytearray and repeatedly append to it.
# xor_key = bytearray()
# for i in range(key_length):
#     xor_key.append(i + 1)

print("xor_key =", xor_key, "= ", end = '')
for byte in xor_key:
    print(binary_rep(byte, 8), end = ' ')
print("")

# Make a Python string of letters.
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

# Use the encode method of Python strings to convert the string
# to a bytes object.
lowercase_bytes = lowercase_letters.encode()
print("lowercase_bytes =", lowercase_bytes)

# We'll be building a bytearray object of XORed bytes.
# A bytes object is immutable (like a Python string).
# A bytearray object is mutable (like a Python list).
xored_lowercase_bytes = bytearray()
print("")

# Process the bytes object 4 bytes at a time, XORing each
# byte in the bytes object with a byte from the key.
block_start = 0
while block_start < len(lowercase_bytes):
    print("new block")

    # Grab the next 4-byte block from the bytes object.
    # Note: It's OK if block_start + key_length goes beyond the end of the bytes object.
    block = lowercase_bytes[block_start : block_start + key_length]

    # XOR each byte in the block with a byte from the key.
    # Append the result to the bytearray object xored_lowercase_bytes.
    for i in range(len(block)):
        xored_byte = block[i] ^ xor_key[i]
        print(block_start + i, chr(block[i]), block[i], binary_rep(block[i], 1), chr(xored_byte),
              xored_byte, binary_rep(xored_byte, 1))
        xored_lowercase_bytes.append(xored_byte)

    # Go on to the next block.
    block_start += len(block)

print("\nxored_lowercase_bytes =", xored_lowercase_bytes)