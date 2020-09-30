from Protocol import Protocol
import FileIO as IO

class ZB(Protocol):
    def __init__(self):
        self.category = 'ZigBee'
        self.protocol = ['wpan:zbee_nwk:zbee_aps:zbee_zcl',
            'wpan:zbee_nwk:zbee_aps:zbee_zcl:zbee_zcl_general.onoff',
            'wpan:zbee_nwk:zbee_aps:zbee_zcl:zbee_zcl_general.level_control',
            'wpan:zbee_nwk:zbee_aps:zbee_zcl:zbee_zcl_lighting.color_ctrl',
            'wpan:zbee_nwk:zbee_aps:zbee_zcl:zbee_zcl_general.ota']
        #self.opcodes = None
        #self.handles = None
        self.zcl = []
        self.package = []

    def load_data(self, filelist):
        super(ZB, self).load_data(filelist[0:2])
        #self.opcodes = IO.load_json(filelist[2])
        #self.handles = IO.load_json(filelist[3])

    def gather(self):
        self.zcl = self.filter(self.protocol)
        idx = 1
        for packet in self.zcl:
            self.package.append(self.pack(packet, idx))
            idx += 1

    def pack(self, packet, idx):
        task = ('Hub' if packet['csv']['src'] == '0x0000' else packet['csv']['src'])
        start = str(idx)
        finish = str(idx + 1)
        resource = packet['frame']['frame.protocols'].split(':')[-1]
        description = packet['csv']['info']
        return dict(Task=task, Start=start, Finish=finish, Resource=resource, Description=description)

    def gen_description(self, packet):
        num = packet['frame']['frame.number']
        time = packet['csv']['arrival']
        seq = packet['zbee_zcl']['zbee_zcl.cmd.tsn']
        #color = packet['zbee_zcl']['Payload']['zbee_zcl_general.level_control.level']
        #kelvin = 1000000 // int(color)
        info = packet['csv']['info']
        #description = 'Frame No. {}<br>Arrived at {}<br>Value: {}<br>Request in Frame {}<br>Info: {}'.format(num, time, value, req, info)
        description = None
        return description
    
    def on_off(self, packet):
        pass

    def level(self, packet):
        pass

    def gen_color_keys(self):
        color_keys = []
        for p in self.protocol:
            color_keys.append(p.split(':')[-1])
        return color_keys