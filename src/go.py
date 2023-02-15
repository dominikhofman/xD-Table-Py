import time
from utils.display import Display, Color, Board
from utils.driver import Driver#, pprint
from effects.manager import Manager
from datetime import datetime
from utils.udp import UdpInterface
from utils.mqtt import Mqtt

exit_flag = False

def call(dr, data):
    global bor
    bor.load(data)


set_hz = 30
get_hz = 20
dis = Display(10, 10)
bor = Board(10, 10)
bor.fill(False)
def abc(data):
    global bor
    bor.data = [(ord(d) > 128) for d in data]


dr = Driver("192.168.1.214", 6454)
# dr = Driver("xd-table.local", 6454)
dr.callbacks.append(abc)
#dr.callbacks.append(call)
dr.start_listening()
dr.calibrate()
m = Manager(bor)
mqtt = Mqtt("mqtt", 1883, m, dr)
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
    #        dr.get_touchscreen()

        effect = m.get()
        effect.step(dt)
        effect.render(dis)
        # dis.save_as_png('tmp/'+effect.__class__.__name__.lower() + '.png')
        print(effect.__class__.__name__)
        dr.set_matrix(dis.serialize())

except KeyboardInterrupt:
    print("Exiting with grace.")

finally:
    dr.exit_flag = True
    mqtt.exit_flag = True
    #ui.exit_flag = True
