import re
import subprocess

output = subprocess.run(['ls','-ltr'],stdout=subprocess.PIPE, text=True)
print(output.stdout)