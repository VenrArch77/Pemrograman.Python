# Program Remote SSH Mikrotik Paramiko, Sys, Time, Getpass, click, Command
from click import command
from sys import stderr, stdin, stdout
from click import password_option
import paramiko, time, sys
from getpass import getpass

# Remote SSH Mikrotik
print("\n.........................................................")
print("Welcome To Mikrotik Server For Studi Kasus Policy Routing")
print(".........................................................\n")

port                = input("Please, enter the SSH port: ")
address             = input("Please, enter the ip address of the mikrotik: ")
username            = input("Please, enter the SSH username: ")
password            = getpass("Please, enter the SSH password: ")
mikrotik_6_49_5     = paramiko.SSHClient()
mikrotik_6_49_5.set_missing_host_key_policy(paramiko.AutoAddPolicy)
mikrotik_6_49_5.connect(port=port,
                hostname=address,
                username=username,
                password=password)

print("\n........................................................")
print("Success Login Mikrotik For Studi Kasus Policy Routing!!")
print("........................................................\n")
                
# Remote Time SSH
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)

# Programs That Automatically Make Mikrotik Commands
print ("Sedang melakukan konfigurasi...\n")
print ("[DONE]\n")

router_client1  =   ["/ip address add address=192.168.0.1/24 interface=ether3 comment=Address_Client"]
router_client2  =   ["/ip dhcp-client add interface=ether1 disable=no comment=ISP1"]
router_client3  =   ["/ip dhcp-client add interface=ether2 disable=no comment=ISP2"]
router_client4  =   ["/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade comment=ISP1"]
router_client5  =   ["/ip firewall nat add chain=srcnat out-interface=ether2 action=masquerade comment=ISP2"]
router_client6  =   ["/ip firewall filter add chain=forward action=add-src-to-address-list address-list=Otomatis_IP_Client log=yes address-list-timeout=00:01:00 comment=Otomatis_IP_Client"]
router_client7  =   ["/ip firewall filter add chain=forward content=www.bola.com dst-address-list=Otomatis_IP_Client action=drop"]
router_client8  =   ["/ip firewall filter add chain=forward content=www.facebook.com dst-address-list=Otomatis_IP_Client action=drop"]
router_client9  =   ["/ip firewall filter add chain=forward content=www.youtube.com dst-address-list=Otomatis_IP_Client action=drop"]
router_client10 =   ["/ip firewall filter add chain=forward content=www.detik.com dst-address-list=Otomatis_IP_Client action=drop"]
router_client11 =   ["/system clock set time-zone-name=Asia/Jakarta time-zone-autodetect=yes"]
router_client12 =   ["/system ntp client set enabled=yes mode=unicast primary-ntp=139.199.214.202 secondary-ntp=202.29.5.13"]
router_client13 =   ["/ip arp add address=192.168.0.2 mac-address=08:00:27:56:AC:A6 interface=ether3"]
router_client14 =   ["/ip firewall mangle add chain=prerouting src-address=192.168.0.2 action=mark-routing new-routing-mark=3.1"]
router_client15 =   ["/ip firewall mangle add chain=prerouting src-address=192.168.0.3 action=mark-routing new-routing-mark=2.1"]
router_client16 =   ["/ip route add dst-address=0.0.0.0/0 gateway=192.168.3.1 routing-mark=3.1"]
router_client17 =   ["/ip route add dst-address=0.0.0.0/0 gateway=192.168.2.1 routing-mark=2.1"]
router_client18 =   ["/ip firewall mangle add chain=forward src-address=192.168.0.0/24 action=mark-packet new-packet-mark=user_upload passthrough=yes"]
router_client19 =   ["/ip firewall mangle add chain=forward dst-address=192.168.0.0/24 action=mark-packet new-packet-mark=user_download passthrough=yes"]
router_client20 =   ["/queue tree add name=bw_user_upload parent=global packet-mark=user_upload queue=default-small priority=8 bucket-size=0.100 max-limit=1M"]
router_client21 =   ["/queue tree add name=bw_user_download parent=global packet-mark=user_download queue=default-small priority=8 bucket-size=0.100 max-limit=2M"]
router_client22 =   ["/system scheduler add name=star on-event=ipfirewallfilternumber1 start-date=jan/1/1970 start-time=23:59:00 interval=3d"]
router_client23 =   ["/system scheduler add name=stop on-event=ipfirewallfilternumber1 start-date=jan/1/1970 start-time=23:59:00 interval=3d"]
router_client24 =   ["/ip firewall filter add chain=forward action=drop"]

# Program Results Making Router Commands

for line in router_client1:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client1 = ["/ip address print"]

for line in router_client2:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client2 = ["/ip dhcp-client print"]

for line in router_client3:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client3 = ["/"]

for line in router_client4:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client4 = ["/ip firewall nat print"]

for line in router_client5:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client5 = ["/"]

for line in router_client6:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client6 = ["/ip firewall filter print"]

for line in router_client7:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client7 = ["/"]

for line in router_client8:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client8 = ["/"]

for line in router_client9:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client9 = ["/"]

for line in router_client10:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client10 = ["/"]

for line in router_client11:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client11 = ["/system clock print"]

for line in router_client12:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client12 = ["/system ntp client print"]

for line in router_client13:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client13 = ["/ip arp print"]

for line in router_client14:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client14 = ["/ip firewall mangle print"]

for line in router_client15:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client15 = ["/"]

for line in router_client16:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client16 = ["/ip route print"]

for line in router_client17:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client17 = ["/"]

for line in router_client18:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client18 = ["/"]

for line in router_client19:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client19 = ["/"]

for line in router_client20:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client20 = ["/queue tree print"]

for line in router_client21:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client21 = ["/"]

for line in router_client22:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client22 = ["/system scheduler print"]

for line in router_client23:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client23 = ["/"]

for line in router_client24:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print_client24 = ["/queue tree print"]

# Create Script Router

for line in print_client1:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client2:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client3:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client4:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client5:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client6:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client7:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client8:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client9:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client10:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client11:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client12:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client13:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client14:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client15:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client16:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client17:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client18:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client19:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client20:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client21:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

for line in print_client22:
    stdin, stdout, stderr = mikrotik_6_49_5.exec_command(line)
print(stdout.read().decode("ascii"))

#Penutup Access Router
mikrotik_6_49_5.close()

print('Input Remote Mikrotik: ', [port, address, username])
print('Input Date Mikrotik: ',  [time_string])
print("\n")