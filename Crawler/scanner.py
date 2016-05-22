import socket
import subprocess
import sys
from datetime import datetime


def tcpScan(port_ls, host):
    ans_port = []
    try:
        for port in port_ls:  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((host, port))
            if result == 0:
                ans_port.append(port)
            sock.close()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    return ans_port


def udpScan(port_ls, host):
    '''
    Use the absence of a response to infer that a port is open. 
    However, if a port is blocked by a firewall, this method will 
    falsely report that the port is open. If the port unreachable 
    message is blocked, all ports will appear open. This method is 
    also affected by ICMP rate limiting.
    '''
    ans_port = []  
    s = socket(AF_INET, SOCK_DGRAM)

    for port in port_ls:
        try:
            data = "UEM"
            s.sendto(data,(host,port))
            s.settimeout(0)
            res = s.recvfrom(1024)
            if res:
                ans_por.append(port)

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()
    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    return ans_port


if __name__ == '__main__':
    port_ls_tcp = [22,80,443]
    port_ls_udp = [53]
    # Ask for input
    remoteServer    = raw_input("Enter a remote host to scan: ")
    remoteServerIP  = socket.gethostbyname(remoteServer)
    print tcpScan(port_ls_tcp)
    print udpScan(port_ls_udp)
