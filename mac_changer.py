import subprocess
from colorama import Fore ,Style

default = "wlp2s0"

print ("[+] Default interface :"+ default)
print(Fore.RED + "press Enter to use the default"+Style.RESET_ALL)
interface = input("interface > ")

if interface == '' :
    interface = default

new_mac = input("New MAC Adress : >")

print("[+] Changing MAC Adress of " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down",shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac ,shell=True)
subprocess.call("ifconfig " + interface + " up",shell=True)
subprocess.call("ifconfig | grep ether",shell=True)

if __name__ == "__main__" :
    pass