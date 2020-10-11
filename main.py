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
    
ble_files = ['./packets/BLE_packets/0920_BLE_Yurim.json', 
    './packets/BLE_packets/0920_BLE_Yurim.csv',
    './opcodes/BLE_opcode.json']

zb_files = ['./packets/ZB_packets/0928_zigbee1.json', 
    './packets/ZB_packets/0928_zigbee1.csv']

wf_files = ['./packets/WiFi_packets/200820.json',
    './packets/WiFi_packets/200820.csv', 
    './opcodes/WF_flag.json',
    './opcodes/WF_custom.json']

if __name__ == '__main__':
    ble = bluetooth(ble_files)
    zb = zigbee(zb_files)
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
    
    
