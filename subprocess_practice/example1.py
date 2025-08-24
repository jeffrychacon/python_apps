import subprocess
import re

ls_out = subprocess.run(["ls","-ltr",'-h'],stdout = subprocess.PIPE,text = True)
print(ls_out)

with open("file.txt",'w') as f:
    f.write(str(ls_out.stdout))
f.close

pattern = r'\bM\w*'
match = re.findall(pattern,ls_out.stdout)
print(match)

