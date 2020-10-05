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
        self.zcl = []
        self.package = []

    def load_data(self, filelist):
        super(ZB, self).load_data(filelist[0:2])

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
        description = self.gen_description(packet)
        return dict(Task=task, Start=start, Finish=finish, Resource=resource, Description=description)

    def gen_description(self, packet):
        num = packet['frame']['frame.number']
        time = packet['csv']['arrival']
        seq = packet['zbee_zcl']['zbee_zcl.cmd.tsn']
        info = packet['csv']['info'].split(',')[0]
        description = '<b>Frame No.</b> {}<br><b>Arrived at</b> {}<br><b>Seqence</b> {}<br><b>Info:</b> {}'.format(num, time, seq, info)
        
        if packet['frame']['frame.protocols'].split('.')[-1] == 'color_ctrl':
            color = packet['zbee_zcl']['Payload']['zbee_zcl_lighting.color_control.color_temp']
            kelvin = 1000000 // int(color)
            description += '<br><b>Color</b>: {} ({}K)'.format(color, kelvin)
        
        #if 'Attribute Field' in packet['zbee_zcl']:
        #   description += attribute_field(packet['zbee_zcl']['Attribute Field'])
        #elif 'Status Record' in packet['zbee_zcl']:
        #   description += status_field(packet['zbee_zcl']['Status Record'])

        return description
    
    def attribute_field(self, packet):        
        pass

    def status_field(self, packet):
        pass

    def gen_color_keys(self):
        color_keys = []
        for p in self.protocol:
            color_keys.append(p.split(':')[-1])
        return color_keys