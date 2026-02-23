import paramiko

host = "localhost"
port = 22
username = "lohith kumar"
password = "kosuru"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddpo())

client.connect(
    hostname=host,
    port = port,
    username = username,
    password = password
)

stdin, stdout, stderr = client.exec_command("whoami")

print(stdout.read().decode())

client.close()