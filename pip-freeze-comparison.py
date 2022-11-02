import re
file1 = open("path_to_file1", "r")
file2 = open("path to file2", "r")
old = [str(re.sub("[0-9=.\n]", "", each)) for each in file1]
new = [str(re.sub("[0-9=.\n]", "", each)) for each in file2]
not_in = [package for package in old if not package in new]
print(not_in)
