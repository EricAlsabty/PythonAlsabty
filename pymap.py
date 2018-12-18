#coding utf-8

import socket
import sys
import os
from colorama import Fore,Style
import time

def scanport(ipaddress,firstport,lastport):
    lastport+=1
    for i in range(firstport,lastport):
        pymap(ipaddress,i)

def pymap (host,port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        print Fore.GREEN+"Connection on the port: ",port,"\t\t Port Open"
        print(Style.RESET_ALL)
        s.send(u"OPEN!")
        s.close()
    except:
        print Fore.RED+"Couldnt connect on the port ",port,"\t Port Close"
        print(Style.RESET_ALL)
def main():
    os.system('cls')

    print"""
_    _      _                           
| |  | |    | |                          
| |  | | ___| | ___ ___  _ __ ___   ___  
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
\  /\  /  __/ | (_| (_) | | | | | |  __/ 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___| 
                                         
                                         
             _____                       
            |_   _|                      
              | | ___                    
              | |/ _ \                   
              | | (_) |                  
              \_/\___/                   
                                         
                                         
    ________   ____  ___  ___  ______        
    | ___ \ \ / /  \/  | / _ \ | ___ \       
    | |_/ /\ V /| .  . |/ /_\ \| |_/ /       
    |  __/  \ / | |\/| ||  _  ||  __/        
    | |     | | | |  | || | | || |           
    \_|     \_/ \_|  |_/\_| |_/\_|           
                                             
                                         
    ________   __  _____  ___            
    | ___ \ \ / / |  ___|/ _ \           
    | |_/ /\ V /  | |__ / /_\ \          
    | ___ \ \ /   |  __||  _  |          
    | |_/ / | |   | |___| | | |          
    \____/  \_/   \____/\_| |_/    


        Un mini nmap du pauvre

    """
    host= raw_input("What is the host scanned : ")
    firstPort = raw_input("What is the first port scanned : ")
    lastPort = raw_input("What is the first port scanned : ")
    print ("\n")
    try:
        firstPort=int(firstPort)
        lastPort=int(lastPort)
    except:
        print "Impossible de convertir les variables"
    start = time.time()
    scanport(host,firstPort,lastPort)
    end = time.time()
    print "Le script dure: ", end - start,"secondes"
main()
