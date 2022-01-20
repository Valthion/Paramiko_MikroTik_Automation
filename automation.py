import paramiko
import os
import sys
import time
from getpass import getpass

try:
 print("====Contoh Network Automation====")

 while True:
  try:
   ip=input("Masukkan file .txt untuk alamat IP : ")
   r_ip=open(ip,"r").readlines()
   break
  except IOError:
   print("File tidak tersedia!")
   continue

 ip_list=[]
 for x in r_ip:
   ip_list.append(x.strip())

 ip_list_ok=[]
 print("\n\nMemeriksa sambungan...")
 for ip in ip_list:
  response=os.system("\nping -c 4 {}".format(ip))

  if response == 0:
   print("\n{} is up  ".format(ip))
   ip_list_ok.append(ip)
  else:
   print("\n{} is down  ".format(ip))

 while True:
  try:
   mikrotik=input("Masukkan nama file konfigurasi: ")
   r_mikrotik=open(mikrotik,"r").readlines()
   break
  except IOError:
   print("File tidak tersedia!")
   continue

 username_mikrotik=input("Username: ")
 password_mikrotik=getpass()

 print("Melakukan konfigurasi....\n")
 for ip in ip_list_ok:
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(hostname=ip,username=username_mikrotik,password=password_mikrotik,allow_agent=False,look_for_keys=False)
  print("Sukses login ke {}".format(ip))
  for config in r_mikrotik:
   ssh_client.exec_command(config)
   time.sleep(1)
  print("Sukses konfigurasi {}\n".format(ip))

except KeyboardInterrupt:
 print("Selesai!")
 sys.exit()