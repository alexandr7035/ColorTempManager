import params
import json
import os
import socket
import manager 

#
# Receives json objects with commands
#
# Possible commands
#
# 1) {"seteState": STATE}
# 2) {"geteState": STATE}
# 3) {"setDayValue": TEMP}
# 4) {"getDayValue": TEMP}
# 5) {"setNightValue"}
# 6) {"getNightValue"}
#
# STATE value must be string (either "enabled" or "disabled")
# TEMP value must be integer (from 1000 to 25000 according to redshift documentation)
#

def main():

    server_port = 9090
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)

    print( 'The server is ready to receive.')

    try:
        while True:
            connection_socket, address = server_socket.accept()
            client_mesg = connection_socket.recv(1024)
            client_mesg = client_mesg.decode()

            print("Received message:", client_mesg)

            server_reply = "".encode()
    
            connection_socket.send(server_reply)
            connection_socket.close()

    except KeyboardInterrupt:
        print("\nServer is stopped by Ctrl-C. Exit")


if __name__ == "__main__":
    main()

