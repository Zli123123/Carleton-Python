import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 44444       # Port to listen on (non-privileged ports are > 1023)

print('\n*** Echo Server v 0.1 started  ***\n')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST, PORT))
s.listen()
conn, addr = s.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("client message:", str(data));
        conn.sendall(data[::-1])    # return string in reverse :)