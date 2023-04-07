import subprocess
subprocess.call("ifconfig enp1s0f1 down",shell=True)
subprocess.call("ifconfig enp1s0f1 hw ether 00:11:22:33:44:66",shell=True)
subprocess.call("ifconfig enp1s0f1 up",shell=True)
subprocess.call("ifconfig",shell=True)


