import wifi
import time
from machine import Pin, Timer

# Declare the LED pin
led = Pin("LED", Pin.OUT)


def blink(hw_timer):
    global led
    for _ in range(6):
        led.toggle()
        time.sleep(0.33)


# Load Wi-Fi Info from default JSON file
wlan = wifi.connect()

# Other options include
# wlan = wifi.connect(path="wifi.json")
# wlan = wifi.connect(ssid="linksys", password="admin")

# Print out the IP Address
status = wlan.ifconfig()
print("Wi-Fi IP: " + status[0])

# Blink the LED upon Wi-Fi Connection with HW Timer
timer = Timer()
timer.init(period=0, mode=Timer.ONE_SHOT, callback=blink)
