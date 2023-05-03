from machine import Pin
from time import sleep
import dht
from machine import Pin, SPI
import gc9a01 as gc9a01
from time import sleep
from machine import Pin, PWM
from utime import sleep
import largefont as font
import smallfont as smallfont
import urandom
import random

relay=Pin(10,Pin.OUT)
relay2=Pin(11,Pin.OUT)
noiseReduction=Pin(23,Pin.OUT)
noiseReduction.high()
auxGround=Pin(15,Pin.OUT)
auxGround.low()
relay.high()
relay2.high()
sensor = dht.DHT22(Pin(14))

button1 = Pin(16, mode=Pin.IN, pull=Pin.PULL_DOWN)
button2 = Pin(17, mode=Pin.IN, pull=Pin.PULL_DOWN)
button3 = Pin(21, mode=Pin.IN, pull=Pin.PULL_DOWN)
button4 = Pin(26, mode=Pin.IN, pull=Pin.PULL_DOWN)
button5 = Pin(27, mode=Pin.IN, pull=Pin.PULL_DOWN)

humidity=0.0
temperature=0.0
sethum=0.0

#from fonts.romfonts import vga2_16x32 as font
#from fonts.romfonts import vga2_8x16 as font2
spi = SPI(0, baudrate=30000000, sck=Pin(2), mosi=Pin(3))
tft = gc9a01.GC9A01(
        spi,
        dc=Pin(18, Pin.OUT),
        cs=Pin(20, Pin.OUT),
        reset=Pin(19, Pin.OUT),
        backlight=Pin(0, Pin.OUT),
        rotation=0)
tft.rotation(0)
tft.fill(gc9a01.WHITE)
upper_bound = 35535
lower_bound = 0

while True:
    #relay.high()
    #relay2.high()
    try:
        sleep(1)     # the DHT22 returns at most one measurement every 2s
        sensor.measure()     # Recovers measurements from the sensor
        print(f"Temperature : {sensor.temperature():.1f}°C")
        print(f"Humidity    : {sensor.humidity():.1f}%")
        color1 = urandom.getrandbits(16)  # 16 bits = 2 bytes = 0 to 65535
        print(color1)
        color2 = urandom.getrandbits(16)  # 16 bits = 2 bytes = 0 to 65535
        print(color2)
        color1 = random.randint(0, upper_bound - 1)
        humidity=sensor.humidity()
        temperature=sensor.temperature()
        tft.text(smallfont," QUANTUM R&D ",70,20,gc9a01.WHITE,gc9a01.RED)
        tft.text(font,"HUMIDITY:",50,40,color1,gc9a01.WHITE)
        tft.text(font," {}% ".format(humidity),60,70,gc9a01.WHITE,color1)
        tft.text(font,"TEMPERATURE:",20,110,color1,gc9a01.WHITE)
        tft.text(font," {}% ".format(temperature),20,130,gc9a01.WHITE,color1)
    except OSError as e:
        print("Failed reception")
        




# Generate a random integer between 0 and (upper_bound - 1)





#tft.text(font,"HUMIDITY: {:04.1f}s".format(setTime),30,50,gc9a01.WHITE,gc9a01.BLACK)
#tft.text(font,"TEMP: {:05.1f}c".format(setTemp),30,100,gc9a01.WHITE,gc9a01.BLACK)
#tft.text(font,"RT.T: {:05.1f}c".format(RTT),30,150,gc9a01.WHITE,gc9a01.BLACK)
