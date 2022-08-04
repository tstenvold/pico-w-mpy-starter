# Pico W Project Starter

This is a project starter for Pico W using MicroPython. It is a simple 
framework for creating a Pico W project that connect to a Wi-Fi network.

## Getting Started

### Clone This Repository

    git clone https://github.com/tstenvold/pico-w-mpy-starter
    cd pico-w-mpy-starter

### Install MicroPython for Raspberry Pi Pico W

Download the latest firmware from [the MicroPython website](https://micropython.org/download/rp2-pico-w/).

Follow the instruction there to install the firmware.
> hold down the BOOTSEL button while plugging the board into USB. The uf2 
file below should then be copied to the USB mass storage device that appears. Once programming of the new firmware is complete the device will automatically reset and be ready for use

### Create Wifi Configuration JSON
In the pico-w-starter directory create a file named wifi_config.json. This 
file should contain the following information:

```json
{
    "ssid": "your-wifi-ssid",
    "password": "your-wifi-password"
}
```

**- ! - Attention - ! -** 

*This file is not included in the repository to prevent users from 
accidentally committing this file to the repository with their own Wifi 
information.*

### Running and Saving to Device via Thonny

You can easily use [Thonny](https://thonny.org/) to run this project and 
interact with the Pico W.

Upload the files ```main.py```, ```wifi.py``` and your ```wifi_config.json``` to root 
directory of the Pico W via Thonny.

Now you can plug your Pico W into any power source and the program will run 
and blink the LED on the Pico W upon successful connection to the Wi-Fi network.

### License
As some of this code is based on the examples from [RaspberryPi](https://github.com/raspberrypi/pico-examples)
I've used the same BSD 3-clause license.

### Issues and Contributions
Please report any issues or feature requests to [github](https://github.com/tstenvold/pico-w-mpy-starter/issues)

### More Info
You can find more information about development on the Pico W from the official sources [Getting started with Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico) and [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)
