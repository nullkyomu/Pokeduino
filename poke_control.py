import serial;
from serial.tools import list_ports;
import time;

import sys
from PyQt5 import QtWidgets
from pokeform import Ui_Form

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

ser = None;

#接続
def connect():
	BAUD_RATE = 115200;

	ports = list_ports.comports() 

	for p in ports:
		port = print(p[0])

	#一番上のポートがAruduinoの奴なことが多いので雑コーディング
	ports[0][0]

	return serial.Serial(ports[0][0],BAUD_RATE)


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


#時渡り
def timeLeap():
	pressButton(HOME,d=1000);
	pressButton(RIGHT)
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
	pressButton(HOME,d=1200);

#アンコールワットバグの操作を行う
#みんなで挑戦を選択する手前の画面で起動する
def encoreWatt():

    pressButton(A,d=2800);

    timeLeap()

    pressButton(B,d=2000);
    pressButton(A,d=6000);
    pressButton(A,d=250);
    pressButton(A,d=250);
    pressButton(A,d=250);


def battleCafe():
	#1分間A連打
	st = time.time();
	while True:
		pressButton(A,t=100,d=200);
		if time.time() - st > 55:
			break;
	
	delay(200)

	#時渡り
	timeLeap();





class Test(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super(Test,self).__init__(parent);
		self.ui = Ui_Form();
		self.ui.setupUi(self)

		self.ui.btn_A.pressed.connect(press_A)
		self.ui.btn_B.pressed.connect(press_B)
		self.ui.btn_X.pressed.connect(press_X)
		self.ui.btn_Y.pressed.connect(press_Y)
		self.ui.btn_home.pressed.connect(press_HOME)
		self.ui.btn_up.pressed.connect(press_UP)
		self.ui.btn_down.pressed.connect(press_DOWN)
		self.ui.btn_left.pressed.connect(press_LEFT)
		self.ui.btn_right.pressed.connect(press_RIGHT)
		self.ui.btn_upleft.pressed.connect(press_UP_LEFT)
		self.ui.btn_upright.pressed.connect(press_UP_RIGHT)
		self.ui.btn_downleft.pressed.connect(press_DOWN_LEFT)
		self.ui.btn_downright.pressed.connect(press_DOWN_RIGHT)

		self.ui.btn_A.released.connect(release_A)
		self.ui.btn_B.released.connect(release_B)
		self.ui.btn_X.released.connect(release_X)
		self.ui.btn_Y.released.connect(release_Y)
		self.ui.btn_home.released.connect(release_HOME)
		self.ui.btn_up.released.connect(release_STICK)
		self.ui.btn_down.released.connect(release_STICK)
		self.ui.btn_left.released.connect(release_STICK)
		self.ui.btn_right.released.connect(release_STICK)
		self.ui.btn_upleft.released.connect(release_STICK)
		self.ui.btn_upright.released.connect(release_STICK)
		self.ui.btn_downleft.released.connect(release_STICK)
		self.ui.btn_downright.released.connect(release_STICK)

		self.ui.btn_func1.released.connect(press_F1)
		self.ui.btn_func2.released.connect(press_F2)
		self.ui.btn_func3.released.connect(press_F3)
		self.ui.btn_func4.released.connect(press_F4)
		self.ui.btn_func5.released.connect(press_F5)

def press_A():
	ser.write([A,PRESS]);
def press_B():
	ser.write([B,PRESS]);
def press_X():
	ser.write([X,PRESS]);
def press_Y():
	ser.write([Y,PRESS]);
def press_HOME():
	ser.write([HOME,PRESS]);
def press_UP():
	ser.write([LSTICK,CENTER,MIN])
def press_DOWN():
	ser.write([LSTICK,CENTER,MAX])
def press_LEFT():
	ser.write([LSTICK,MIN,CENTER])
def press_RIGHT():
	ser.write([LSTICK,MAX,CENTER])
def press_UP_LEFT():
	ser.write([LSTICK,MIN,MIN])
def press_UP_RIGHT():
	ser.write([LSTICK,MAX,MIN])
def press_DOWN_LEFT():
	ser.write([LSTICK,MIN,MAX])
def press_DOWN_RIGHT():
	ser.write([LSTICK,MAX,MAX])


def release_A():
	ser.write([A,RELEASE]);
def release_B():
	ser.write([B,RELEASE]);
def release_X():
	ser.write([X,RELEASE]);
def release_Y():
	ser.write([Y,RELEASE]);
def release_HOME():
	ser.write([HOME,RELEASE]);

def release_STICK():
	ser.write([LSTICK,CENTER,CENTER])

def press_F1():
	encoreWatt();

def press_F2():
	N = 3;
	for i in range(N):
		encoreWatt();
		delay(500)

def press_F3():
	battleCafe();

def press_F4():
	for i in range(24):
		battleCafe();
		delay(1000);

def press_F5():
	pass;


if __name__ == "__main__":
	ser = connect();
	"""#アンコールワットをN回繰り返し
	N = 500;
	for i in range(N):
		encoreWatt();
		delay(500)
"""
	app = QtWidgets.QApplication(sys.argv);
	window = Test();


	window.show();
	sys.exit(app.exec_());

	
