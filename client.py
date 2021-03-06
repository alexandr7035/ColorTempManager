import socket
import json

import params


class Client():
    def __init__(self):
        # Connect to the server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((params.SERVER_ADDR, params.SERVER_PORT))

    def check_if_enabled(self):
        self.socket.sendall(json.dumps({"command": "getValue", "type": "is_enabled"}).encode())
        response = json.loads(self.socket.recv(1024).decode())

        return response["response"]

    def set_enabled(self, is_enabled):
        self.socket.sendall(json.dumps({"command": "setValue", "type": "is_enabled", "value": is_enabled}).encode())

    def get_day_temp_value(self):
        self.socket.sendall(json.dumps({"command": "getValue", "type": "day_temp"}).encode())
        response = json.loads(self.socket.recv(1024).decode())

        return int(response["response"])

    def set_day_temp_value(self, value):
        self.socket.sendall(json.dumps({"command": "setValue", "type": "day_temp", "value": value}).encode())
