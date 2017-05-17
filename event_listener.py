from socketio_client.manager import Manager
import gpio as led
import gevent
from gevent import monkey

monkey.patch_socket()

io = Manager('moodlight.cloudapp.net', 3000)
moodlamp = io.socket('/')

def turn_on_lamp(state):
    led.reset()
    if state == 'anger':
        led.redOn()
    elif state == 'joy':
        led.yellowOn()
    elif state == 'disgust':
        led.greenOn()
    elif state == 'sad':
        led.blueOn()
    elif state == 'contempt':
        led.magentaOn()
    elif state == 'surprise':
        led.whiteOn()
    elif state == 'fear':
        led.cyanOn()


@moodlamp.on_connect()
def moodlamp_connect():
    print('connect')


@moodlamp.on('state_changed')
def on_hello(*args):
    current_state = args[0].encode("utf-8")
    turn_on_lamp(current_state)
    print(current_state)


moodlamp.connect()
gevent.wait()

