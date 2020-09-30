from Protocol import Protocol
import FileIO as IO

class BLE(Protocol):
    def __init__(self):
        self.category = 'BLE'
        self.protocol = ['nordic_ble:btle:btl2cap:btatt']
        self.opcodes = None
        self.handles = None
        self.btatt = []
        self.package = []

    def load_data(self, filelist):
        super(BLE, self).load_data(filelist[0:2])
        self.opcodes = IO.load_json(filelist[2])
        self.handles = IO.load_json(filelist[3])

    def gather(self):
        self.btatt = self.filter(self.protocol)
        idx = 1
        for packet in self.btatt:
            self.package.append(self.pack(packet, idx))
            idx += 1

    def pack(self, packet, idx):
        task = ('Phone' if packet['csv']['src'] == 'Master' else 'LED')
        start = str(idx)
        finish = str(idx + 1)
        for op in self.opcodes:
            if op['opcode'] == packet['btatt']['btatt.opcode']:
                resource = op['message']
                break
        description = self.gen_description(packet)
        return dict(Task=task, Start=start, Finish=finish, Resource=resource, Description=description)

    def gen_description(self, packet):
        num = packet['frame']['frame.number']
        time = packet['csv']['arrival']
        value = (packet['btatt']['btatt.value'] if 'btatt.value' in packet['btatt'] else '-')
        req = (packet['btatt']['btatt.request_in_frame'] if 'btatt.request_in_frame' in packet['btatt'] else '-')
        info = packet['csv']['info']
        description = 'Frame No. {}<br>Arrived at {}<br>Value: {}<br>Request in Frame {}<br>Info: {}'.format(num, time, value, req, info)
        return description
    
    def gen_color_keys(self):
        color_keys = []
        for op in self.opcodes:
            color_keys.append(op['message'])
        return color_keys