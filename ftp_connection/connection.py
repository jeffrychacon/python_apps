import paramiko

hostname = 'localhost'
port = 21
username = 'username'
password = 'password'

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Be cautious with AutoAddPolicy in production
try:
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password)
except paramiko.AuthenticationException:
    print("Authentication failed. Check username and password/key.")
except paramiko.SSHException as e:
    print(f"SSH connection failed: {e}")

sftp_client = ssh_client.open_sftp()
