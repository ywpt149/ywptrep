__author__ = 'hly'
import socket
def add(ip,port):
    cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cs.settimeout(5)
    address=(str(ip),int(port))
    cs.connect(address)
    cs.close()
#wo shi master
add('10.1.23.139',80)
#wo shi dud
#woshi 123