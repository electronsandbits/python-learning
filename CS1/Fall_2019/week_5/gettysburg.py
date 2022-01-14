'# gettysburg.py
# CS 1 demo by THC to write a file.
# It writes the file gettysburg.txt into the project folder in the workspace.

out_file = open('gettysburg.txt', 'w')
out_file.write('Four score and seven years ago,\n')
out_file.write('our fathers brought forth on this continent, a new nation,\n')
out_file.write('conceived in Liberty, and dedicated to the proposition ')
out_file.write('that all men are created equal.\n')
out_file.close()
