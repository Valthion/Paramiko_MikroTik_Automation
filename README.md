# Paramiko_MikroTik_Automation
An example for network automation in MikroTik using Python and Paramiko

Prerequisites: Configured routers (IP addresses) with username and password

* To use it, make two different .txt files.
* One consists of IP addresses of each routers and one consists of router configuration that will be executed.
* Put it in the same folder with the .py script
* When you're asked for the address (Masukkan file .txt untuk alamat IP), type your .txt file which has addresses.
* Then, type your .txt file name which has configs when you're asked for the config file (Masukkan nama file konfigurasi)
* The script will check your routers by pinging 4 times before the address added to the arrays
* Config process will start after you entered the username and password of the router (Each router should have the same user and pass)

Execute the script by typing in terminal/cmd: python3 automation.py
This script could be used to execute any kind of configuration that is supported by the router, so make sure your config file is in .txt and each syntaxes typed properly
