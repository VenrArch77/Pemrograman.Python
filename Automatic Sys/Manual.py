import sys
from zipfile import ZipFile

file_program = sys.argv[0]
no_py = sys.argv[1]
program = sys.argv[2]
total_file = sys.argv

file_read = open(sys.argv[0], "r")
print("Input File: ", file_read.name)

file_content = file_read.readlines()

print("Open File: ", file_content)

file_read.close()

with ZipFile(sys.argv[1], mode='w') as file:

    file.write(sys.argv[2])
    file.write(sys.argv[3])
    file.write(sys.argv[4])
    file.write(sys.argv[5])
    file.write(sys.argv[6])
    
    print('Loading... ' + no_py)
    print('Success... ' + no_py)
    print('Total File:' , total_file)

file.close()