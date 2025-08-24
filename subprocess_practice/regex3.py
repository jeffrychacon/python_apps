import re

with open("output.txt",'r') as f:
    data = f.read()
f.close()

pattern = r'\bStepping:\s+(\d){1,}\b'
found = re.search(pattern,data)
print(found.group(1))