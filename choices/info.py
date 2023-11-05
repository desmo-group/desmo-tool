import colorama
import time 
import platform
import subprocess
from colorama import Fore, Back, Style

print(Fore.RED + """



                         ██████╗ ███████╗▄▄███▄▄·███╗   ███╗ ██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
                         ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═████╗    ██║████╗  ██║██╔════╝██╔═══██╗
                         ██║  ██║█████╗  ███████╗██╔████╔██║██║██╔██║    ██║██╔██╗ ██║█████╗  ██║   ██║
                         ██║  ██║██╔══╝  ╚════██║██║╚██╔╝██║████╔╝██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
                         ██████╔╝███████╗███████║██║ ╚═╝ ██║╚██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
                         ╚═════╝ ╚══════╝╚═▀▀▀══╝╚═╝     ╚═╝ ╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                              

                                           ╔═══            INFO           ═══╗
                                           ║                                 ║
                                           ║       Github > Desmo-Group      ║    
                                           ║       Discord > .gg/desmo       ║
                                           ║       Press enter to exit       ║
                                           ║                                 ║
                                           ╚═══                           ═══╝
                                                
    """)
back = input("""
                                                            """)
if back == str(""):
    with open("desmo.py", "r", encoding="utf-8") as file:
        code = file.read()
    clear_screen()
    exec(code)
else:
    with open("choices/info.py", "r", encoding="utf-8") as file:
        code = file.read()
    clear_screen()
    exec(code)