import subprocess

def command1():
    output = subprocess.run(['top','-l1','-n','1'],stdout=subprocess.PIPE,text=True)
    output2 = subprocess.run(['vm_stat','-l'],stdout=subprocess.PIPE,text=True)
    print(output2)

command1()