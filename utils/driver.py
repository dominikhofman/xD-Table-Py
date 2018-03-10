import socket
import threading
import time

class Driver(object):
    PING = 0x0
    PONG = 0x1
    SET_MATRIX = 0x2
    GET_TOUCHSCREEN = 0x3
    GET_TOUCHSCREEN_RAW = 0x4
    GET_REFFERENCE_TABLE = 0x5
    TOUCHSCREEN = 0x6
    TOUCHSCREEN_RAW = 0x7
    REFFERENCE_TABLE = 0x8
    CALIBRATE = 0x9
    RESET = 0xa
    PANIC = 0x45
    ARTNET = 0x41

    def __init__(self, ip="127.0.0.1", port=1337):
        self.ip = ip 
        self.port = port
        self.connected = False

        self.address = (ip, port)

        # create socket
        self.sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
        self.sock.settimeout(3)

    def start_listening(self):
        t = threading.Thread(target=self.receive_thread)
   #     t.deamon = True
        t.start()

    def send_data(self, data):
        try:
            self.sock.sendto(bytearray(data), self.address)
        except IOError as e:
            print ("Network Error")
            time.sleep(1)

    def set_matrix(self, data):
        self.send_data([Driver.SET_MATRIX, len(data) / 3] + data)

    def ping(self):
        self.send_data([Driver.PING])

    def calibrate(self):
        self.send_data([Driver.CALIBRATE])

    def get_refference_table(self):
        self.send_data([Driver.GET_REFFERENCE_TABLE])

    def reset(self):
        self.send_data([Driver.RESET])

    def get_touchscreen(self):
        self.send_data([Driver.GET_TOUCHSCREEN])

    def get_touchscreen_raw(self):
        self.send_data([Driver.GET_TOUCHSCREEN_RAW])

    def receive_thread(self):
        global exit
        while not exit:
            msg, client = self.sock.recvfrom(1024) 
            msg = msg[1:]
            printt(msg)
            frame = []
            for e in msg:
                frame += [0, 0, e]
            self.set_matrix(frame)
#            if ord(msg[0]) == Driver.TOUCHSCREEN:
            #print("Got response: \n{}".format(", ".join("0x{:02X}".format( ord(c)) for c in msg)))



def printt(data):
    buff = ""
    for i, d in enumerate(data):
        buff += "{:02X} ".format(ord(d))
        if (i + 1) % 10 == 0:
            print (buff)
            buff = ""
    print("\n")

if __name__ == "__main__":
    dr = Driver("192.168.1.6", 6454)

    dr.start_listening()

#    dr.calibrate()

    try:
        while True:
            frame = [255,0,0 ,0,255,0 ,0,0,255]
            dr.set_matrix(frame)
            dr.get_touchscreen()
            time.sleep(0.05)

    except KeyboardInterrupt:
        global exit
        exit = True
     

