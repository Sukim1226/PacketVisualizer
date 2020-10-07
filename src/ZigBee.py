from .Protocol import Protocol

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

    def load(self, filelist):
        super(ZB, self).load_packets(filelist[0:2])

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
        
        # cmd.id: 0 // Read Attributes
        # cmd.id: 1 // Read Attributes Response
        # cmd.id: 10 // Report Attributes
        # cmd.id: 11 // Default Response
        #if packet['zbee_zcl']['zbee_zcl.cmd.id'] == '0':
        #   description += attribute_field(packet['zbee_zcl']['Attribute Field'])
        #elif packet['zbee_zcl']['zbee_zcl.cmd.id'] == '1':
        #   description += status_record(packet['zbee_zcl']['Status Record'])

        return description
    
    def attribute_field(self, packet):        
        pass

    def status_record(self, packet):
        pass

    def gen_color_keys(self):
        color_keys = []
        for p in self.protocol:
            color_keys.append(p.split(':')[-1])
        return color_keys