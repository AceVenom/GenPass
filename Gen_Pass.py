import string
import random
import time 
import os
class colori:
    verde = '\033[92m' #GREEN
    giallo = '\033[93m' #YELLOW
    rosso = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

print(colori.verde + """..######...########.##....##....########.....###.....######...######.
.##....##..##.......###...##....##.....##...##.##...##....##.##....##
.##........##.......####..##....##.....##..##...##..##.......##......
.##...####.######...##.##.##....########..##.....##..######...######.
.##....##..##.......##..####....##........#########.......##.......##
.##....##..##.......##...###....##........##.....##.##....##.##....##
..######...########.##....##....##........##.....##..######...######. """)
print(colori.giallo + "----------------------------------------#Password-Generation-------------------------------------------")
print("--------------------")
print("Author: AceVenom    |")
print("--------------------")
print("---------Menu--------")
nome = input("insert name: ")
time.sleep(1)
cognome = input("insert surname: ")
time.sleep(1)
print("""   ___ ___ _  _ ___ ___    _ _____ ___ ___  _  _ 
  / __| __| \| | __| _ \  /_\_   _|_ _/ _ \| \| |
 | (_ | _|| .` | _||   / / _ \| |  | | (_) | .` |
  \___|___|_|\_|___|_|_\/_/ \_\_| |___\___/|_|\_|
                                                 """)
time.sleep(1)
def simboli():
 simbolo = "!"
simbolo2 = "?"
simbolo3 = "^"
simbolo4 = "$"
simbolo5 = "*"
simbolo6 = "."
simbolo7 = "_"
print(colori.rosso + "password with simbols: " + simbolo4 + simbolo3  + nome + simbolo5 + simbolo2 + simbolo4 + cognome )
def numeri():
 numero1 = "0"
numero2 = "1"
numero3 = "2"
numero4 = "3"
numero5 = "4"
numero6 = "5"
numero7 = "6"
numero8 = "7"
numero9 = "8"
numero10 = "9"
numero11 = "10"
print("password with numbers: " + numero2 + cognome + numero5 + nome + numero11)
def misto():
 print("password with simbols and numbers: " + simbolo4 + numero11 + nome + simbolo7 + simbolo6 + numero2 + cognome + numero10 + simbolo5)  
def pulizia():
 time.sleep(1)
simboli()
time.sleep(1)
numeri()
time.sleep(1)
misto()
pausa = input("insert any button for continue...")




