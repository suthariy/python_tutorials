import paramiko

k = paramiko.RSAKey.from_private_key_file("/Users/Documents/awspair/key-pair-name.pem")
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting")
ssh_client.connect(hostname="hostname or ip",
                   port=22,
                   username='ec2-user',
                   password=k)
print("Connected")

"""
stdin,stdout, stderr = ssh_client.exec_command("sudo ls")
stdin.write("mypassword\n")
print(stdout.readlines())
print(stderr.readlines)
ssh_client.close()
"""

ftp_client = ssh_client.open_sftp()
ftp_client.get("/tmp/test.txt","/Users/Downloads/test2.txt")
ftp_client.close()
