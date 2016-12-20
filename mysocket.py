import socket

class mysocket:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(0.0001)

    def myhost(self, host, port):
        print 'Awaiting connection'
        self.sock.bind((host,port))
        self.sock.listen(1)
        flag=0
        while flag==0:
            try:
                self.connection, client_address = self.sock.accept()
                flag=1
            except:
                pass   # re-enters the loop
        print 'Connected to ', self.connection, client_address

    def myconnect(self, host, port):
        print 'Awaiting connection'
        flag=0
        while flag==0:
            try: 
                self.sock.connect((host, port))
                flag=1
            except:
                pass  # re-enters the loop
        print "Connected"

    def mysend(self, msg):
        try:
            self.sock.sendall(msg)
        except:
            print "Failed to send to socket"
            return 0

    def myreceive(self, length):
        try:
            msg=self.connection.recv(length)
            return msg
        except:
            return 0