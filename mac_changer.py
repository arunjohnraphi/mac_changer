import subprocess


interface = input("interface > hint enp1s0f1 >")
new_mac = input("New MAC Adress : >")

print("[+] Changing MAC Adress of " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac ,shell=True)
subprocess.call("ifconfig " + interface + " up",shell=True)
subprocess.call("ifconfig | grep ether",shell=True)

