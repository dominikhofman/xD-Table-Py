import socket
import threading



class Key(object):
    def __init__(self, key):
        self.char = key

class UdpInterface(object):
    def __init__(self, on_press, port):
        self.on_press = on_press
        self.port = port
        self.exit_flag = False
        # self.ip = "127.0.0.1" # only localhost
        self.ip = ""# all interfaces

        t = threading.Thread(target=self.worker)
        t.start()



    # Collect events until released
    def worker(self):
        sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
        sock.bind((self.ip, self.port))

        while not self.exit_flag:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
            try:
                self.exit_flag = not self.on_press(Key(str(data)))
            except: pass


