import re
import os
os.system('cls')
regex_pattern = r""
list = re.split(regex_pattern, input())
n = []
for i in list:
    if i != '' and i != ',' and i != '.':
        n.append("".join(i))
