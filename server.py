import params
import json
import os
import socket
import manager 


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

