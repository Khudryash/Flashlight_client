from socket import *
import json
from .flashlight import Flashlight
import threading


def server_messages_handler():
    while True:
        msg = client.recv(2048)
        if msg:
            message = json.loads(msg.decode(FORMAT))
            if message["command"] == "ON":
                flashlight.on()
            elif message["command"] == "OFF":
                flashlight.off()
            elif message["command"] == "COLOR":
                flashlight.color(message["metadata"])

SERVER = "192.168.1.70"
PORT = 7000
ADDR = (SERVER, PORT)
FORMAT = "utf-8"

client = socket(AF_INET, SOCK_STREAM)

flashlight = Flashlight(client)
client.connect(ADDR)
handler = threading.Thread(target=server_messages_handler)
handler.start()

flashlight.run()
