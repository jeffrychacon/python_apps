import re

with open("output.txt",'r') as f:
    data = f.read()
f.close()
#print(data)

pattern = r'CPU\(s\):\s+(\d+)'

match = re.search(pattern,data)
print(match.group(1))