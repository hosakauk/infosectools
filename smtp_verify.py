import socket
import sys

if len(sys.argv) != 3:
    print("Usage: %s %s %s" % (sys.argv[0], "<host>", "<username_list>"))
    sys.exit(0)

host = sys.argv[1]
usernames = sys.argv[2]

def smtp_check(usernames):
    f = open(usernames)
    for i in f:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((host, 25))
        banner = s.recv(1024)
        print(banner)
        s.send('VRFY ' + i + '\r\n')
        result = s.recv(1024)
        print(result)
        s.close()
smtp_check(usernames)

          
