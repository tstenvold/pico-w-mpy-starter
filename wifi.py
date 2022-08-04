import network
import time
import json


def _load_wifi_info(path):
    with open(path) as fp:
        data = json.loads(fp.read())
        if data["ssid"] and data["password"]:
            return data["ssid"], data["password"]
        else:
            raise ValueError("No ssid or password in config file")


def _try_connect(wlan, max_wait=10):
    while max_wait > 0 and wlan.status() < 3:
        if wlan.status() < 0:
            raise RuntimeError("network connection failed")
        max_wait -= 1
        time.sleep(1)

    return wlan
        
        
def connect(ssid=None, password=None, path="wifi_config.json"):
    
    if ssid is None or password is None:
        ssid, password = _load_wifi_info(path)
        
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
     
    wlan = _try_connect(wlan)
    
    if wlan.status() == 3:
        return wlan
    
    raise RuntimeError("network connection failed")