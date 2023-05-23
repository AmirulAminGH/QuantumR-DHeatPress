
import random
from machine import Pin, SPI
import gc9a01py as gc9a01
from time import sleep
from machine import Pin, PWM
from utime import sleep
from max6675 import MAX6675

import _thread

# Choose a font

# from fonts import vga1_8x8 as font
# from fonts import vga2_8x8 as font
# from fonts import vga1_8x16 as font
# from fonts import vga2_8x16 as font
# from fonts import vga1_16x16 as font
# from fonts import vga1_bold_16x16 as font
# from fonts import vga2_16x16 as font
# from fonts import vga2_bold_16x16 as font
# from fonts import vga1_16x32 as font
# from fonts import vga1_bold_16x32 as font
# from fonts import vga2_16x32 as font
from fonts.romfonts import vga2_16x32 as font
from fonts.romfonts import vga2_8x16 as font2
spi = SPI(0, baudrate=60000000, sck=Pin(2), mosi=Pin(3))
tft = gc9a01.GC9A01(
        spi,
        dc=Pin(18, Pin.OUT),
        cs=Pin(20, Pin.OUT),
        reset=Pin(19, Pin.OUT),
        backlight=Pin(0, Pin.OUT),
        rotation=0)

setTime=20.0
setTemp=110.0
setTarget=110.0
RTT=0.0
TRGT=0.0

modeselect="PTOP"
modecycle=1

selectvar=1
varvalue=1


button1 = Pin(16, mode=Pin.IN, pull=Pin.PULL_DOWN)
button2 = Pin(17, mode=Pin.IN, pull=Pin.PULL_DOWN)
button3 = Pin(21, mode=Pin.IN, pull=Pin.PULL_DOWN)
button4 = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)
button5 = Pin(27, mode=Pin.IN, pull=Pin.PULL_DOWN)

buzzer = PWM(Pin(8))

sck = Pin(14, Pin.OUT)
cs = Pin(15, Pin.OUT)
so = Pin(12, Pin.IN)

sensor = MAX6675(sck, cs , so)

sck2 = Pin(14, Pin.OUT)
cs2 = Pin(13, Pin.OUT)
so2 = Pin(12, Pin.IN)

sensor2 = MAX6675(sck2, cs2 , so2)

relay1   = Pin(10, mode=Pin.OUT)
relay2   = Pin(11, mode=Pin.OUT)
relay1.on()
relay2.on()
deltaOffset=1
def main():
    

    while True:
        for rotation in range(8):
            tft.rotation(rotation)
            tft.fill(0)
            col_max = tft.width - font.WIDTH*6
            row_max = tft.height - font.HEIGHT

            for _ in range(25):
                tft.text(
                    font,
                    "Hello!",
                    random.randint(0, col_max),
                    random.randint(0, row_max),
                    gc9a01.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8)),
                    gc9a01.color565(
                        random.getrandbits(8),
                        random.getrandbits(8),
                        random.getrandbits(8))
                )
def pageInit():
    tft.rotation(0)
    tft.fill(gc9a01.WHITE)
def mainPage():
    global selectvar
    
    if selectvar==1:
        tft.text(font2,"QUANTUM R&D",75,10,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TIME: {:04.1f}s".format(setTime),30,40,gc9a01.WHITE,gc9a01.BLACK)
        tft.text(font,"PTOP: {:05.1f}c".format(RTT),30,80,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TRGT: {:05.1f}c".format(TRGT),30,120,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"MODE:{}".format(modeselect),30,160,gc9a01.BLACK,gc9a01.WHITE)
    if selectvar==2:
        tft.text(font2,"QUANTUM R&D",75,10,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TIME: {:04.1f}s".format(setTime),30,40,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"PTOP: {:05.1f}c".format(setTemp),30,80,gc9a01.WHITE,gc9a01.BLACK)
        tft.text(font,"TRGT: {:05.1f}c".format(TRGT),30,120,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"MODE:{}".format(modeselect),30,160,gc9a01.BLACK,gc9a01.WHITE)
    if selectvar==3:
        tft.text(font2,"QUANTUM R&D",75,10,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TIME: {:04.1f}s".format(setTime),30,40,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"PTOP: {:05.1f}c".format(RTT),30,80,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TRGT: {:05.1f}c".format(setTarget),30,120,gc9a01.WHITE,gc9a01.BLACK)
        tft.text(font,"MODE:{}".format(modeselect),30,160,gc9a01.BLACK,gc9a01.WHITE)
    if selectvar==4:
        tft.text(font2,"QUANTUM R&D",75,10,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TIME: {:04.1f}s".format(setTime),30,40,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"PTOP: {:05.1f}c".format(RTT),30,80,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TRGT: {:05.1f}c".format(TRGT),30,120,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"MODE:{}".format(modeselect),30,160,gc9a01.WHITE,gc9a01.BLACK)
    if selectvar==5:
        tft.text(font2,"QUANTUM R&D",75,10,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TIME: {:04.1f}s".format(setTime),30,40,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"PTOP: {:05.1f}c".format(RTT),30,80,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"TRGT: {:05.1f}c".format(TRGT),30,120,gc9a01.BLACK,gc9a01.WHITE)
        tft.text(font,"MODE:{}".format(modeselect),30,160,gc9a01.BLACK,gc9a01.WHITE)
        


def button():
    global setTime
    global setTemp
    global setTarget
    global sensor
    global selectvar
    global varvalue
    global modeselect
    global modecycle
    
    global TRGT
    global sensor2
    
    
    if selectvar==1:
        if button1.value() == 1:
            setTime+=1
            tet()
        if button2.value() == 1:
            setTime-=1
            tet()
    if selectvar==2:
        if button1.value() == 1:
            setTemp+=1
            tet()
        if button2.value() == 1:
            setTemp-=1
            tet()
    if selectvar==3:
        if button1.value() == 1:
            setTarget+=1
            tet()
        if button2.value() == 1:
            setTarget-=1
            tet()
    if selectvar==4:
        if button1.value() == 1:
            modecycle+=1
            tet()
        if button2.value() == 1:
            modecycle-=1
            tet()
        if modecycle>2:
            modecycle=1
        if modecycle<1:
            modecycle=2
        
        if modecycle==1:
            modeselect="PTOP"
        if modecycle==2:
            modeselect="TRGT"
            








    if button3.value() == 1:
        selectvar+=1
        if selectvar>5:
            selectvar=1
        tet()
        #mainPage()
        #print("button 3 is pressed")
    if button4.value() == 1:
        setTemp-=1
        tet()
        #mainPage()
        #print("button 4 is pressed")
    if button5.value() == 1:
        print("going down")
        warning()
        if modecycle==1:
            relay2.off()
            tempstr=setTime
            while setTime>0:
                sleep(1)
                setTime-=1
            setTime=tempstr
            relay2.on()
        if modecycle==2:
            relay2.off()
            while TRGT < setTarget:
                sleep(0.25)
            relay2.on()

        #mainPage()
        #print("button 5 is pressed")
    
        
def tet():
    global buzzer
    buzzer.freq(2000)
    buzzer.duty_u16(10000)
    sleep(0.1)
    buzzer.duty_u16(0)
def tut():
    global buzzer
    buzzer.freq(3000)
    buzzer.duty_u16(10000)
    sleep(0.1)
    buzzer.duty_u16(0)
    sleep(0.1)
    buzzer.freq(3000)
    buzzer.duty_u16(10000)
    sleep(0.1)
    buzzer.duty_u16(0)
def warning():
    global buzzer
    buzzer.freq(500)
    buzzer.duty_u16(10000)
    sleep(0.5)
    buzzer.duty_u16(0)
    sleep(0.5)
    buzzer.duty_u16(10000)
    sleep(0.5)
    buzzer.duty_u16(0)
    sleep(0.5)
    buzzer.duty_u16(10000)
    sleep(0.5)
    buzzer.duty_u16(0)
    sleep(0.5)

def second_thread():
    global RTT
    global setTemp
    global deltaOffset
    global relay1
    global TRGT
    global sensor
    global sensor2
    cycle=0
    sleep(2)
    while True:
        RTT=sensor.read()
        TRGT=sensor2.read()
        if RTT<(setTemp-deltaOffset):
            relay1.off()
            if cycle==0:
                tut()
                cycle=1
        if RTT>(setTemp+deltaOffset):
            relay1.on()
            if cycle==1:
                tut()
                cycle=0
       
        mainPage()

_thread.start_new_thread(second_thread,())
pageInit()
mainPage()

while True:
    button()
    sleep(0.1)
    #RTT=sensor.read()
    #TRGT=sensor2.read()
    #mainPage()
    

