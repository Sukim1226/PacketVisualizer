from FileIO import IO

class BLE(IO):
    def __init__(self, filelist):
        self.datas = self.load_json(filelist[0])
        self.datas_csv = self.load_csv(filelist[1])
        self.opcodes = self.load_json(filelist[2])
        self.handles = self.load_json(filelist[3])
        self.gatt = []

    def filter(self):
        for d in self.datas:
            packet = d['_source']['layers']
            if packet['frame']['frame.protocols'] == 'nordic_ble:btle:btl2cap:btatt':
                c = self.get_csv(int(packet['frame']['frame.number']))
                packet['csv'] = c
                self.gatt.append(packet)

    def get_csv(self, frame_num):
        dic = {}
        dic['src'] = self.datas_csv[frame_num - 1]['Source'].split('_')[0]
        dic['arrival'] = self.datas_csv[frame_num - 1]['Time']
        #dic['dst'] = self.datas_csv[frame_num - 1]['Destination']
        dic['info'] = self.datas_csv[frame_num - 1]['Info']
        return dic

    def gather(self):
        package = []
        idx = 1
        for g in self.gatt:
            package.append(self.pack(g, idx))
            idx += 1
        return package

    def gen_color_key(self):
        keys = []
        for op in self.opcodes:
            keys.append(op['message'])
        return keys

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