import subprocess

def capture_top_output(output_file):
    try:
        result = subprocess.run(['top','-l1','-n','1'], stdout=subprocess.PIPE, text=True)
        with open(output_file,'w') as file:
            file.write(result.stdout)
    except Exception as e:
        print(f'An error has occurred: {e}')


output_file = 'output_file.txt'
capture_top_output(output_file)