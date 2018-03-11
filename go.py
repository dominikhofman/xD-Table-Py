import time
from display import Display, Color, Board
from driver import Driver#, pprint
from effects.manager import Manager
from datetime import datetime
from udp import UdpInterface
from mqtt import Mqtt

exit_flag = False


def on_press(key):
    try:
        key = key.char
    except:
        print('wirdo char')
        return

    global m
    if key == 'p':
        # exit
        global exit_flag
        exit_flag = True
        return

    if key == 'e':
        # next effect
        m.next()
        return

    if key == 'q':
        # prev effect
        m.prev()
        return

    m.on_press(key)


def call(dr, data):
    global bor
    bor.load(data)


set_hz = 30
get_hz = 1
dis = Display(10, 10)
bor = Board(10, 10)
bor.fill(False)
dr = Driver("192.168.1.6", 6454)
#dr.callbacks.append(call)
#dr.start_listening()
#dr.calibrate()
m = Manager(bor)
mqtt = Mqtt("127.0.0.1", 1883, m)
#ui = UdpInterface(on_press, 4444)

set_start = datetime.now()
get_start = datetime.now()
try:
    while not exit_flag:
        time.sleep(1.0 / set_hz)
        dt = (datetime.now() - set_start).total_seconds()
        set_start = datetime.now()

        if (datetime.now() - get_start).total_seconds() > (1.0 / get_hz):
            get_start = datetime.now()
            #dr.get_touchscreen()

        effect = m.get()
        effect.step(dt)
        effect.render(dis)
        dr.set_matrix(dis.serialize())

except KeyboardInterrupt:
    print("Exiting with grace.")

finally:
    dr.exit_flag = True
    mqtt.exit_flag = True
    #ui.exit_flag = True
