import os
# Specify the directory you want to list
directory = '/'
contents = os.listdir(directory)
for entry in contents:
    print(entry)