import params
import json
import os
import socket
import atexit
import subprocess

from apscheduler.schedulers.background import BackgroundScheduler


class Manager:
    def __init__(self):

        # Create working directory
        if not os.path.isdir(params.WORK_DIR):
            os.mkdir(params.WORK_DIR)

        if not os.path.exists(params.CONFIG_FILE):

            self.config = open(params.CONFIG_FILE, 'w')

            default_settings = {}

            default_settings["day_temp"] = params.TEMP_DAY_DEFAULT_VALUE
            default_settings["night_temp"] = params.TEMP_NIGHT_DEFAULT_VALUE
            default_settings["is_enabled"] = False

            json.dump(default_settings, self.config)

            self.config.close()

        self.config = open(params.CONFIG_FILE, 'r+')
        self.settings = json.load(self.config)

    def update_settings_file(self):
        self.config.seek(0)
        json.dump(self.settings, self.config)
        self.config.truncate()

    def handle_GET_request(self, json_request):

        data = {}
        data["response"] = self.settings[json_request["type"]]

        return json.dumps(data).encode()

    def handle_SET_request(self, json_request):
        self.settings[json_request["type"]] = json_request["value"]

    def activate_redshift(self):
        # os.system("redshift -P -O " + str(self.settings["day_temp"]))
        subprocess.check_call(['redshift', "-P",  "-O", str(self.settings["day_temp"])], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def stop_redshift(self):
        # os.system("redshift -x")
        subprocess.check_call(['redshift', "-x"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    def update_timejob(self):
        if self.settings["is_enabled"]:
            self.activate_redshift()
        else:
            self.stop_redshift()


def main():

    server_port = 9090
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)

    manager = Manager()

    # Timejob for updates
    # Use 'atexit' to shut down the scheduler when exiting the app
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=manager.update_timejob,
                      trigger="interval",
                      seconds=params.UPDATE_DELAY)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())

    print('The server is ready to receive.')

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

                response = b""

                if (client_mesg["command"] == "getValue"):
                    response = manager.handle_GET_request(client_mesg)

                elif (client_mesg["command"] == "setValue"):
                    manager.handle_SET_request(client_mesg)

                print("Response sent: " + str(response))
                connection_socket.send(response)

            connection_socket.close()

    # Exit on Ctrl-C
    except KeyboardInterrupt:
        print("\nServer is stopped by Ctrl-C. Exit")


if __name__ == "__main__":
    main()
