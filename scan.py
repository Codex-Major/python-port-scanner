from datetime import datetime
startTime = datetime.now()
import socket
import threading
import sys

def scan(ip,p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, p))
    if result == 0:
        print ("[+] Found port: {}".format(p))
    s.close()

def main():
    try:
        try:
            print('*'*100)
            host = sys.argv[1]
        except IndexError:
            host = input("Enter a remote host to scan: ")
        ip = socket.gethostbyname(host)
        print (f"[*] Scanning {host}...")
        print ('*'*100)
        print(f"[*] Scan started at: {startTime}")
        for p in range(1025):
            t = threading.Thread(target=scan, args=[ip, p] )
            t.start()
    except KeyboardInterrupt:
        print ("[!] You pressed Ctrl+C. Exiting!")
        sys.exit()
    except socket.gaierror:
        print ("Hostname could not be resolved... Exiting!")
        sys.exit()
    except socket.error:
        print (f"Could not connect to {host}... Exiting!")
        sys.exit()

main()
endTime = datetime.now()
print(f'[*] Scan ended at: {endTime}')
totalTime =  endTime - startTime
print(f'[*] Scan completed in: {totalTime}')
exit(0)
