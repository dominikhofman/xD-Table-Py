import paho.mqtt.client as mqtt
import threading
import json

class Mqtt(object):
    def __init__(self, host, port, manager):
        self.host = host
        self.port = port
        self.manager = manager
        self.exit_flag = False

        t = threading.Thread(target=self.worker)
        t.start()


    # Collect events until released
    def worker(self):

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

        self.client.connect(host=self.host, port=self.port)

        while not self.exit_flag:
            self.client.loop()

        self.client.disconnect()

    def on_connect(self, client, userdata, flags, rc):
        print("Mqtt connected with result code " + str(rc))

        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe("home/xdtable/effect/set")

    def on_message(self, client, userdata, msg):
        # egz {"effect": {"color": {"r": 255, "b": 455, "g": 455}, "idx": 2}}
        m = json.loads(msg.payload)
        self.manager.set(m['idx'])
