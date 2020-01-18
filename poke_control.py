import serial;
from serial.tools import list_ports;
import time;


RIGHT = 0
LEFT = 1
UP = 2
DOWN = 3
A = 4
B = 5
X = 6
Y = 7
R = 8
L = 9
ZR = 10
ZL = 11
RSTICK = 12
LSTICK = 13
RCLICK = 14
LCLICK = 15
HOME = 16
CAPTURE = 17
PLUS = 18
MINUS = 19

PRESS = 0
RELEASE = 1

MIN = 0
CENTER = 128
MAX = 255


#接続
BAUD_RATE = 115200;

ports = list_ports.comports() 

for p in ports:
    port = print(p[0])

#一番上のポートがAruduinoの奴なことが多いので雑コーディング
ports[0][0]

ser = serial.Serial(ports[0][0],BAUD_RATE)


def pressButton(btn,t=80,d=100):
    ser.write([btn,PRESS]);
    time.sleep(t/1000);
    ser.write([btn,RELEASE]);

    time.sleep(d/1000)

def moveStick(stickType,xstick,ystick,t,d=0):
    if xstick == RIGHT:
        xstick = MAX;
    elif xstick == LEFT:
        xstick = MIN;
    else:
        xstick = CENTER;

    if ystick == UP:
        ystick = MAX;
    elif ystick == DOWN:
        ystick = MAX;
    else:
        ystick = CENTER;
    ser.write([stickType,xstick,ystick]);
    ser.write([stickType,xstick,ystick]);

    time.sleep((t/1000));

    ser.write([stickType,CENTER,CENTER])

    time.sleep(d/1000)

#Aruduino Studioのそれに合わせてms単位
def delay(t):
    time.sleep((t/1000))


# %%
pressButton(A,100)
#moveStick(LSTICK,CENTER,UP,1000)



#アンコールワットバグの操作を行う
#みんなで挑戦を選択する手前の画面で起動する
def ancoreWatt():

    pressButton(A,d=2800);

    pressButton(HOME,d=1000);

    pressButton(RIGHT);

    pressButton(RIGHT);

    pressButton(DOWN);

    pressButton(RIGHT);


    pressButton(A);
    delay(50);

    pressButton(DOWN,2500);
    pressButton(A);

    pressButton(DOWN,80,150);
    pressButton(DOWN,80,150);
    pressButton(DOWN,80,150);
    pressButton(DOWN,80,150);
    pressButton(A);
    delay(200);
    pressButton(DOWN,100,150);
    pressButton(DOWN,100,150);
    pressButton(A,d=100);

    pressButton(RIGHT,50,80);
    pressButton(RIGHT,50,80);
    pressButton(UP,50,80);
    pressButton(RIGHT,50,80);
    pressButton(RIGHT,50,80);
    pressButton(RIGHT,50,80);
    pressButton(A);
    pressButton(HOME,d=1000);
    pressButton(HOME,d=1000);

    pressButton(B,d=2000);
    pressButton(A,d=6000);
    pressButton(A,d=250);
    pressButton(A,d=250);
    pressButton(A,d=250);


if __name__ == "__main__":
	#アンコールワットをN回繰り返し
	N = 500;
	for i in range(N):
		ancoreWatt();
		delay(500)


ser.close()

