import cmd
from getpass import getpass
from sys import stderr, stdin, stdout
import paramiko

print("\n.........................................................")
print("Welcome To Mikrotik Server For Studi Kasus Policy Routing")
print(".........................................................\n")

port        = input("Masukan Port SSH Anda: ")
address     = input("Masukan Address SSH Anda: ")
username    = input("Masukan Username SSH Anda: ")
password    = getpass("Masukan Password SSH Anda: ")

print("\n.........................................................")
print("Success Remote To Mikrotik Server")
print(".........................................................\n")

try:
    mikrotik_6_49_5     = paramiko.SSHClient()
    mikrotik_6_49_5.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    mikrotik_6_49_5.connect(port=port,
                hostname=address,
                username=username,
                password=password)
    while True:
        try:
            cmd = input("[admin@Mikrotik] > ")
            if cmd == "exit": break
            stdin, stdout, stderr = mikrotik_6_49_5.exec_command(cmd)
            print(stdout.read().decode())
        except KeyboardInterrupt:
            break
    mikrotik_6_49_5.close()
except Exception as client:
    print(str(client))

print("\n.........................................................")
print("Thanks For Access Mikrotik Server")
print(".........................................................\n")