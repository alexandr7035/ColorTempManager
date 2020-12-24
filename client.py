import socket
import params
import json

class Client():
    def __init__(self):
        # Connect to the server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((params.SERVER_ADDR, params.SERVER_PORT))

    
    def get_state(self):
        self.socket.sendall(json.dumps({"command": "getValue", "type" : "state"}).encode())
        
        #print(self.socket.recv(1024).decode())

        response = json.loads(self.socket.recv(1024).decode())

        return response["response"]

    def get_day_temp_value(self):
        self.socket.sendall(json.dumps({"command": "getValue", "type" : "temp", "time" : "day"}).encode())
        response = json.loads(self.socket.recv(1024).decode())
        
        return int(response["response"])


