#
# Chat Sever ver 0.3.1
# 

import socket    
import select
import threading

global usrList

class userInfo :
    def __init__(self, name) :
        self.name = name
        self.msgSender = ''
        self.msgBuf = ''
    

def clientServerT(clientsocket, addr):

    # registration section
    while True :
        
        clientsocket.sendall(b'\r\nEnter your name: ')
        while True :
            usrName = clientsocket.recv(1024)
            usrNameStr = usrName.decode("utf-8")
            if usrNameStr != '\r\n' :
                break
        try :
            x = usrList[usrNameStr]
        except :
            break  # go to chat section          
        else :     # stay in the registration loop
            clientsocket.sendall(b'*** Such a user name is already exists, try another one ...\r\n')            
    
    # chat section    
    clientsocket.sendall(b'***  Welcome \'' + usrName + b'\' to our ChatServer v 0.3  ***\r\n')
    usrList[usrNameStr] = userInfo(usrNameStr)
    
    while True:
        
        # check either message arrived
        if usrList[usrNameStr].msgBuf :
            clientsocket.sendall(b'You\'d got message from: \'' + usrList[usrNameStr].msgSender.encode('utf-8') + b'\' MSG: ')
            clientsocket.sendall(usrList[usrNameStr].msgBuf.encode('utf-8'))
            clientsocket.sendall(b'\r\n')
            usrList[usrNameStr].msgBuf = ''
            usrList[usrNameStr].msgSender = ''
    
        # asyncronious I/O in use!!!
        timeout = 1  # set timeout to 1 sec
        readySockets, _, _ = select.select([clientsocket], [], [], timeout)
        if readySockets : 
            netMsg = clientsocket.recv(1024)   # THIS IS THE BLOCKING CALL!!!
        else :
            continue
        
        msgStr = netMsg.decode("utf-8").strip()
        param = msgStr.split(' ', 2)
        cmd = param[0].lower()
        
        if cmd  == '' : # ignore an empty command
            continue
        elif cmd == 'list' :
             clientsocket.send(b'Active users list:\r\n')
             for usr in usrList:
                 clientsocket.send('\t'.encode('utf-8'))
                 if usr == usrNameStr :
                     clientsocket.send(b'*')
                 clientsocket.send(usr.encode('utf-8'))
                 clientsocket.send('\n\r'.encode('utf-8'))
        elif cmd == 'logout' :
            clientsocket.sendall(b'***  Leaving the chat room  ***\r\n')
            # remove client from the active list
            del usrList[usrNameStr]
            break

        elif cmd == "send" :
            # do something here: send <user name> <"messge"> so SPLITTING is required!!!
            if param[1] == '@all' :
                 for usr in usrList:
                     usrList[usr].msgSender = usrNameStr
                     usrList[usr].msgBuf = param[2]
            else :
                if param[1] in usrList :
                    usrList[param[1]].msgSender = usrNameStr
                    usrList[param[1]].msgBuf = param[2]
                else :
                    clientsocket.sendall(b'Unknown sender name\r\n')
        elif cmd == "birthday":
            if param[1] in usrList :
                    birthdayperson = param[1]
                    clientsocket.sendall(("happy birthday, ").encode ('utf-8'))
                    clientsocket.sendall(birthdayperson.encode ('utf-8'))
                    clientsocket.sendall("\n\r".encode ('utf-8'))
        elif cmd == "msend": 
            #multi send 
            #for i in range(len(int(param[1]))):
               # if param[1] in usrList:
                    
        elif cmd == "help":
            instructions = ["logout", "send", "mutlisend", "birthday", "description - in work"] 
            clientsocket.send(b'Instructions list:\r\n')
            for k in range(len(instructions)):
                data = instructions[k]
                clientsocket.send(data.encode("utf-8"))
                clientsocket.send('\n\r'.encode('utf-8'))
        else :
           clientsocket.sendall(b'Error unknown command: ' + cmd.encode('utf-8') + '\n\r'.encode('utf-8'))
    clientsocket.close()


if __name__ == '__main__' :
    
    s = socket.socket()         # Create a socket object
    host = '127.0.0.1'          # Get local machine name 'myhost.com'
    port = 44444                # Reserve a port for your service.
    
    print('Chat Server started! Waiting for clients...')
    
    s.bind((host, port))        # Bind to the port
    s.listen(5)                 # Now wait for client connection.
    
    usrList = {}                # Active user information dictionary {user_name : userInfo_instance}
    
    while True:
       c, addr = s.accept()     # Establish connection with client. THIS IS THE BLOCKING CALL!!!
       print('Got connection from', addr)
       newChat = threading.Thread(target=clientServerT, args=(c, addr))
       newChat.start()
       
    s.close()
