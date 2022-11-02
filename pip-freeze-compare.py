import re
file1 = open("/Users/libinmathew/Downloads/prod_pip_freeze.txt", "r")
file2 = open("/Users/libinmathew/Downloads/current.txt", "r")
old = [str(re.sub("[0-9=.\n]", "", each)) for each in file1]
new = [str(re.sub("[0-9=.\n]", "", each)) for each in file2]
not_in = [package for package in old if not package in new]
print(not_in)
