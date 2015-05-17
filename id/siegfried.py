from __future__ import print_function
 
import socket
import subprocess
import sys
 
def file_tool(path):
    return subprocess.check_output(['file', path]).strip()
    
def main(path):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        sock.connect('/tmp/siegfried')
        sock.sendall(path)
        reply = sock.recv(1024)
        if reply.startswith('e'):
            if reply.startswith('error: format unknown'):
                if "text" in file_tool(path):
                    print("x-fmt/111")
                    return 0
            print("Siegfried sent {}.".format(reply), file=sys.stderr)
            return 1
        else:
            print(reply)
    except socket.error, msg:
        print("Siegfried connection failed {}".format(msg), file=sys.stderr)
        return 1
 
if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
