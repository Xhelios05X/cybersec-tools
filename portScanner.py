#!/bin/python3

import socket
import sys

def scanner(IPaddress:str, portRange:int):
    port = 1
    scanner = socket.socket()
    while port <= portRange:
        try:
            scanner.connect((IPaddress,port))
        except:
            pass
        else:
            print(f"port {port} is open")
        
        port += 1

if __name__ == "__main__":
    IPaddress = sys.argv[1]
    portRange = int(sys.argv[2])
    scanner(IPaddress, portRange)