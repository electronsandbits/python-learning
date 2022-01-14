in_file = open("alphabet.txt", "rb")

plaintext_block = in_file.read(16)
while len(plaintext_block) > 0:
    print(plaintext_block)
    plaintext_block = in_file.read(16)

in_file.close()
