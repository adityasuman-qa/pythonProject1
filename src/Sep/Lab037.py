# file

import os

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+ "/example.txt"
    file = open(full_path_file, 'r')
    print(file.read())
except Exception as e:
    print("File ia not found, fix a path or create a file")

finally:
    try:
        file.close()
    except NameError as ne:
        print(ne)

