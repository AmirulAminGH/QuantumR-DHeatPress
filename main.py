"""
hello.py

    Writes "Hello!" in random colors at random locations on the display

"""
import random
from machine import Pin, SPI
import gc9a01py as gc9a01
from time import sleep
from machine import Pin, PWM
from utime import sleep
from max6675 import MAX6675

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

setTime=10.0
setTemp=25.0
RTT=0.0

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

relay1   = Pin(10, mode=Pin.OUT)
relay2   = Pin(11, mode=Pin.OUT)
relay1.on()
relay2.on()
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
    tft.fill(0)
def mainPage():
    tft.text(font2,"QUANTUM R&D",75,10,gc9a01.RED,gc9a01.BLACK)
    tft.text(font,"TIME: {:04.1f}s".format(setTime),30,50,gc9a01.WHITE,gc9a01.BLACK)
    tft.text(font,"TEMP: {:05.1f}c".format(setTemp),30,100,gc9a01.WHITE,gc9a01.BLACK)
    tft.text(font,"RT.T: {:05.1f}c".format(RTT),30,150,gc9a01.WHITE,gc9a01.BLACK)

def button():
    global setTime
    global setTemp
    global sensor
    if button1.value() == 1:
        setTime+=1
        tet()
        #mainPage()
        #print("button 1 is pressed")
    if button2.value() == 1:
        setTime-=1
        tet()
        #mainPage()
        #print("button 2 is pressed")
    if button3.value() == 1:
        setTemp+=1
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
        relay2.off()
        sleep(setTime)
        relay2.on()
        #mainPage()
        #print("button 5 is pressed")
    
        
def tet():
    global buzzer
    buzzer.freq(2000)
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
    
pageInit()
mainPage()
deltaOffset=5
while True:
    button()
    RTT=sensor.read()
    mainPage()
    if RTT<(setTemp-deltaOffset):
        relay1.off()
    if RTT>(setTemp+deltaOffset):
        relay1.on()


