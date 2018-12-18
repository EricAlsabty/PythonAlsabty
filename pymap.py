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
        s.send()
        s.close()
    except:
        print Fore.RED+"Couldnt connect on the port ",port,"\t Port Close"
        print(Style.RESET_ALL)

def main():
    os.system('cls')
    print """

       /$$   /$$ /$$      /$$  /$$$$$$  /$$$$$$$                         
      | $$$ | $$| $$$    /$$$ /$$__  $$| $$__  $$                        
      | $$$$| $$| $$$$  /$$$$| $$  \ $$| $$  \ $$                        
      | $$ $$ $$| $$ $$/$$ $$| $$$$$$$$| $$$$$$$/                        
      | $$  $$$$| $$  $$$| $$| $$__  $$| $$____/                         
      | $$\  $$$| $$\  $ | $$| $$  | $$| $$                              
      | $$ \  $$| $$ \/  | $$| $$  | $$| $$                              
      |__/  \__/|__/     |__/|__/  |__/|__/                              
                                                                          
                                                                           
                                                                           
               /$$$$$$$  /$$   /$$                                         
              | $$__  $$| $$  | $$                                         
              | $$  \ $$| $$  | $$                                         
              | $$  | $$| $$  | $$                                         
              | $$  | $$| $$  | $$                                         
              | $$  | $$| $$  | $$                                         
              | $$$$$$$/|  $$$$$$/                                         
              |_______/  \______/                                          
                                                                           
                                                                           
                                                                           
       /$$$$$$$   /$$$$$$  /$$   /$$ /$$    /$$ /$$$$$$$  /$$$$$$$$      
      | $$__  $$ /$$__  $$| $$  | $$| $$   | $$| $$__  $$| $$_____/      
      | $$  \ $$| $$  \ $$| $$  | $$| $$   | $$| $$  \ $$| $$            
      | $$$$$$$/| $$$$$$$$| $$  | $$|  $$ / $$/| $$$$$$$/| $$$$$         
      | $$____/ | $$__  $$| $$  | $$ \  $$ $$/ | $$__  $$| $$__/         
      | $$      | $$  | $$| $$  | $$  \  $$$/  | $$  \ $$| $$            
      | $$      | $$  | $$|  $$$$$$/   \  $/   | $$  | $$| $$$$$$$$      
      |__/      |__/  |__/ \______/     \_/    |__/  |__/|________/      
                                                                   

         Un mini nmap du pauvre
    """
    host= raw_input("What is the host scanned : ")
    firstPort = raw_input("What is the first port scanned : ")
    lastPort = raw_input("What is the last port scanned : ")
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
