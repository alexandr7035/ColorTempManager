import params
import json
import os
import socket


#
# Receives json objects with commands
#
# Possible commands
#
# 1) {"setState": STATE}
# 2) {"geteState": STATE}
# 3) {"setDayValue": TEMP}
# 4) {"getDayValue": TEMP}
# 5) {"setNightValue"}
# 6) {"getNightValue"}
#
# STATE value must be string (either "enabled" or "disabled")
# TEMP value must be integer (from 1000 to 25000 according to redshift documentation)
#



class Manager:
    def __init__(self):
        if not os.path.exists(params.CONFIG_FILE):

            self.config = open(params.CONFIG_FILE, 'w')

            default_settings = {}

            default_settings["day_value"] = params.TEMP_DAY_DEFAULT_VALUE
            default_settings["night_value"] = params.TEMP_NIGHT_DEFAULT_VALUE
            default_settings["is_enabled"] = False

            json.dump(default_settings, self.config)

            self.config.close()

        self.config = open(params.CONFIG_FILE, 'r+')
        self.settings = json.load(self.config)



    def check_if_enabled(self):
        return self.settings['is_enabled']



def main():

    server_port = 9090
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)

    manager = Manager()

    print( 'The server is ready to receive.')

    # Main loop
    # Receive and handle commands
    try:
        while True:
            connection_socket, address = server_socket.accept()
            
            while True: 
                client_mesg = connection_socket.recv(1024)

                print("Received message:", client_mesg)

                try:
                    client_mesg = json.loads(client_mesg.decode())
                except json.decoder.JSONDecodeError:
                    break
                

                response = ""

                print("OK")

                if (client_mesg["command"] == "getValue"):
                    print("OK")
                    if (client_mesg["type"] == "state"):
                        data = {}
                        data["response"] = manager.settings['is_enabled']

                        response = json.dumps(data).encode()

                    elif (client_mesg["type"] == "temp"):
                        print("OK")
                        if (client_mesg["time"] == "day"):
                            data = {}
                            data["response"] = manager.settings["day_value"]

                            response = json.dumps(data).encode()

                print("RESP " + response.decode())
                connection_socket.send(response)
                
            connection_socket.close()

    # Exit on Ctrl-C
    except KeyboardInterrupt:
        print("\nServer is stopped by Ctrl-C. Exit")


if __name__ == "__main__":
    main()

