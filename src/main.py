from BLE import BLE
from GUI import GUI

def bluetooth(filelist):
    ble = BLE(files)
    ble.filter()
    datas = ble.gather()
    color_key = ble.gen_color_key()
    return 'BLE', datas, color_key



files = ['../packets/BLE_packets/0920_BLE_Yurim.json', 
    '../packets/BLE_packets/0920_BLE_Yurim.csv',
    '../opcodes/BLE_opcode.json', '../opcodes/BLE_handle.json']

protocol, datas, color_key = bluetooth(files)

gui = GUI(protocol, datas, color_key)
gui.show()
    
    
