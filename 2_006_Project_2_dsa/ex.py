## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
#print (os.listdir("."))

# Let us check if this file is indeed a file!
#print (os.path.isfile("./ex.py"))

# Does the file end with .py?
#print ("./ex.py".endswith(".py"))

path = "./testdir"
suffix = 'c'
list_dir = os.listdir(path)
print(list_dir)
for d_name in list_dir:
    d_name_path = os.path.join(path,d_name)
    if os.path.isfile(d_name_path) and d_name.endswith(suffix):
        print(d_name_path)

path2 = os.path.join(path,list_dir[3])
print(path2)
# list_dir2 = os.listdir(path2)
# print(list_dir2)

# for root,d_names,f_names in os.walk(path):
    #print (root)
    #print (d_names)
    # print (f_names)
