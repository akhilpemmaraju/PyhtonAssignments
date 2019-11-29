# mobile number
# from the current working directory read log files and email in that files
import re
import os
# number = input("Enter thr phone number : ")
# numberpattern = '^[789][0-9]{9}$'
# match = re.search(numberpattern, number)
# if match:
#     print("Valid Number")
# else:
#     print("Invalid Number")

import os
pattern = "\\s[a-zA-Z][\\w]+@[\\w]+[.][a-zA-Z]+|^[a-zA-Z][\\w]+@[\\w]+[.][a-zA-Z]+"
for f in list(filter(lambda ff: os.path.splitext(ff)[1] == ".log", os.listdir())):
    for line in open("{0}".format(f), "r"):
        match = re.search(pattern, line)
        if match:
            print(line)
