from ZigBee import ZB
from BLE import BLE
from GUI import GUI

def bluetooth(filelist):
    ble = BLE()
    ble.load_data(filelist)
    ble.gather()
    return ble
    
def zigbee(filelist):
    zb = ZB()
    zb.load_data(filelist)
    zb.gather()
    return zb
    

def wifi(filelist):
    pass

ble_files = ['../packets/BLE_packets/0920_BLE_Yurim.json', 
    '../packets/BLE_packets/0920_BLE_Yurim.csv',
    '../opcodes/BLE_opcode.json', '../opcodes/BLE_handle.json']

zb_files = ['../packets/ZB_packets/0928_zigbee1.json', 
    '../packets/ZB_packets/0928_zigbee1.csv']

if __name__ == '__main__':
    ble = bluetooth(ble_files)
    zb = zigbee(zb_files)
    gui = GUI()
    gui.add(ble)
    gui.add(zb)

    # command: 'BLE', 'ZigBee', 'Wi-Fi', 'ALL'
    gui.show('ZigBee')
    gui.show('BLE')
    
    
