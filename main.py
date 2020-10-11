from src.WIFI import WF
from src.ZigBee import ZB
from src.BLE import BLE
from src.GUI import GUI

def bluetooth(filelist):
    ble = BLE()
    ble.load(filelist)
    ble.gather()
    return ble

def zigbee(filelist):
    zb = ZB()
    zb.load(filelist)
    zb.gather()
    return zb

def wifi(filelist):
    wf = WF()
    wf.load(filelist)
    wf.gather()
    return wf

ble_files = []

zb_files = []

wf_files = []

if __name__ == '__main__':
    ble_files.append('./packets/BLE_packets/' + argv[1] + '.json')
    ble_files.append('./packets/BLE_packets/' + argv[1] + '.csv')
    ble = bluetooth(ble_files)

    zb_files.append('./packets/ZB_packets/' + argv[2] + '.json')
    zb_files.append('./packets/ZB_packets/' + argv[2] + '.csv')
    zb = zigbee(zb_files)

    wf_files.append('./packets/WiFi_packets/' + argv[3] + '.json')
    wf_files.append('./packets/WiFi_packets/' + argv[3] + '.csv')
    wf = wifi(wf_files)

    gui = GUI()
    gui.add(ble)
    gui.add(zb)
    gui.add(wf)

    # command: 'BLE', 'ZigBee', 'WiFi', 'ALL'
    gui.show('ZigBee')
    gui.show('BLE')
    gui.show('WiFi')
    #gui.show('ALL')
