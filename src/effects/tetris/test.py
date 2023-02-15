import socket
import threading
import time


class Driver(object):
    def __init__(self, ip="127.0.0.1", port=1337):
        self.ip = ip 
        self.port = port
        self.connected = False

        # create socket
        self.sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP

    def connect():
        pass
        
    def send_frame(self, frame):
         frame = bytearray([2, len(frame) / 3] + frame)
         self.sock.sendto(frame,
                          (self.ip, self.port))

    def start_listening(self):
        t = threading.Thread(target=self.receive_thread)
        t.start()


    def receive_thread(self):
        while True:
           msg, client = self.sock.recvfrom(1024) 
           print(msg)

if __name__ == "__main__":
    dr = Driver()
    dr.start_listening()
    while True:
        dr.send_frame([97, 98, 99, 100, 101, 102])
        time.sleep(1)
