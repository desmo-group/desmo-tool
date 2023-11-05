import colorama
import time 
import platform
import subprocess
import os
import re
import io
import sys
import time
import json
import ctypes
import random
import zipfile
import requests
import pkg_resources
import subprocess
import threading
import multiprocessing
import keyboard
import base64
import colorama
import shutil
import os.path
import string
import tempfile
import time
import webbrowser
import urllib.request
from zipfile import ZipFile
from time import sleep
from colorama import Fore
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from distutils.version import LooseVersion
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from colorama import Fore, Back, Style

def clear_screen():
    subprocess.run(["cls"], shell=True)
clear_screen()

pcname = (os.getenv('COMPUTERNAME'))
proxycount = str(9022)
notyet = "COMING SOON"

print(Fore.RED + """


                                                                                                           │ Proxies
                         ██████╗ ███████╗▄▄███▄▄·███╗   ███╗ ██████╗     ████████╗ ██████╗  ██████╗ ██╗    │""" + notyet + """
                         ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═████╗    ╚══██╔══╝██╔═████╗██╔═████╗██║    └─────────
                         ██║  ██║█████╗  ███████╗██╔████╔██║██║██╔██║       ██║   ██║██╔██║██║██╔██║██║     
                         ██║  ██║██╔══╝  ╚════██║██║╚██╔╝██║████╔╝██║       ██║   ████╔╝██║████╔╝██║██║     
                         ██████╔╝███████╗███████║██║ ╚═╝ ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
                         ╚═════╝ ╚══════╝╚═▀▀▀══╝╚═╝     ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  
  [BUY] PREMIUM                                     [UPD] UPDATE                                        [TM] By DE$M0™                                                               

     ╔═══        COMING SOON        ═══╗   ╔═══        Everything         ═══╗   ╔═══        COMING SOON        ═══╗
     ║                                 ║   ║                                 ║   ║                                 ║
     ║                                 ║   ║           [ 1 ] DDOS            ║   ║                                 ║
     ║                                 ║   ║                                 ║   ║                                 ║
     ╚═══                           ═══╝   ╚═══                           ═══╝   ╚═══                           ═══╝
 

""")
choice = input("""
                                                            """)
if choice == str(1):
    with open("choices/ddos.py", "r", encoding="utf-8") as file:
        code = file.read()
    clear_screen()
    exec(code)
elif choice.lower() == "tm":
    with open("choices/info.py", "r", encoding="utf-8") as file:
        code = file.read()
    clear_screen()
    exec(code)
else:
    with open("desmo.py", "r", encoding="utf-8") as file:
        code = file.read()
    clear_screen()
    exec(code)