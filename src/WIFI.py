from Protocol import Protocol
import FileIO as IO

class WF(Protocol):
    def __init__(self):
        self.category = 'WiFi'
        self.protocol = ['eth:ethertype:ip:tcp',
            'eth:ethertype:ip:tcp:tls']
        self.flags = None
        self.ipmap = None
        self.tcp = []
        self.package = []

    def load_data(self, filelist):
        super(WF, self).load_data(filelist[0:2])
        self.flags = IO.load_json(filelist[2])
        self.ipmap = IO.load_json(filelist[3])

    def gather(self):
        self.tcp = self.filter(self.protocol)
        idx = 1
        for packet in self.tcp:
            p = self.pack(packet, idx)
            if p != None:
                self.package.append(self.pack(packet, idx))
            idx += 1

    def pack(self, packet, idx):
        task = self.match_name(packet['csv']['src'])
        if task == None:
            return None
        start = str(idx)
        finish = str(idx + 1)
        resource = None
        for f in self.flags:
            if f['flag'] == packet['tcp']['tcp.flags']:
                resource = f['message']
                break
        description = self.gen_description(packet)
        return dict(Task=task, Start=start, Finish=finish, Resource=resource, Description=description)

    def gen_description(self, packet):
        num = packet['frame']['frame.number']
        time = packet['csv']['arrival']
        dst = self.match_name(packet['ip']['ip.dst_host'])
        dstIP = packet['ip']['ip.dst']
        info = packet['csv']['info']
        description = '<b>Frame No.</b> {}<br><b>Arrived at</b> {}<br><b>Destination:</b> {} ({})<br><b>Info:</b> {}'.format(num, time, dst, dstIP, info)
        return description

    def match_name(self, s):
        for ip in self.ipmap:
            if ip['IP'] == s:
                return ip['Name']

        l = s.split('.')
        if l[-2] == 'amazonaws':
            return 'Cloud'
        elif l[-2] == 'smartthings':
            return 'Smartthings API'
        else:
            return None

    def gen_color_keys(self):
        color_keys = []
        for f in self.flags:
            color_keys.append(f['message'])
        return color_keys