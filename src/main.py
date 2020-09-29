from BLE import BLE
from GUI import GUI

def bluetooth(filelist):
    ble = BLE()
    ble.load_data(filelist)
    ble.gather()

    gui = GUI(ble)
    gui.show()
    



files = ['../packets/BLE_packets/0920_BLE_Yurim.json', 
    '../packets/BLE_packets/0920_BLE_Yurim.csv',
    '../opcodes/BLE_opcode.json', '../opcodes/BLE_handle.json']

bluetooth(files)


    
    
