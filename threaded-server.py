import socket               # Import socket module
import threading

def clientServerT(clientsocket, addr):
    print('*** Client Server started', addr)
    while True:
        msg = clientsocket.recv(1024)
        #do some checks and if msg == someWeirdSignal: break:
        print(addr, ' >> ', msg)
        
        clientsocket.sendall(msg)
        if msg == 'Logout' :
            break
    clientsocket.close()

s = socket.socket()         # Create a socket object
host = '127.0.0.1' # Get local machine name
port = 44444                # Reserve a port for your service.

print('Server started!')
print ('Waiting for clients...')

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.


while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   threading.Thread(target=clientServerT, args=(c, addr)).start()
   
s.close()
