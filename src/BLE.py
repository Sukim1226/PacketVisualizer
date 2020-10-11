from .Protocol import Protocol

class BLE(Protocol):
    def __init__(self):
        self.category = 'BLE'
        self.protocol = ['nordic_ble:btle:btl2cap:btatt']
        self.opcodes = None
        self.btatt = []
        self.package = []

    def load(self, filelist):
        self.load_packets(filelist[0:2])
        self.opcodes = self.load_data(filelist[2])

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
        resouce = None
        for op in self.opcodes:
            if op['opcode'] == packet['btatt']['btatt.opcode']:
                resource = op['message']
                break
        description = self.gen_description(packet)
        return dict(Task=task, Start=start, Finish=finish, Resource=resource, Description=description)

    def gen_description(self, packet):
        num = packet['frame']['frame.number']
        time = packet['csv']['arrival']
        value = ('<br><b>Value:</b> ' + packet['btatt']['btatt.value'] 
            if 'btatt.value' in packet['btatt'] else None)
        req = ('<br><b>Request in Frame:</b> ' + packet['btatt']['btatt.request_in_frame'] 
            if 'btatt.request_in_frame' in packet['btatt'] else '-')
        info = packet['csv']['info']
        description = '<b>Frame No.</b> {}<br><b>Arrived at</b> {}{}{}<br><b>Info:</b> {}'.format(num, time, value, req, info)
        return description
    
    def gen_color_keys(self):
        color_keys = []
        for op in self.opcodes:
            color_keys.append(op['message'])
        return color_keys