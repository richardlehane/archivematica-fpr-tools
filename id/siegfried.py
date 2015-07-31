from __future__ import print_function
 
import socket
import sys
 
def main(path):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect('/tmp/siegfried')
        sock.sendall(path)
        reply = sock.recv(1024)
        if reply.startswith('error'):
            print("Siegfried sent {}.".format(reply), file=sys.stderr)
            return 1
        else:
            print(reply)
    except socket.error, msg:
        print("Siegfried connection failed {}".format(msg), file=sys.stderr)
        return 1
 
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
