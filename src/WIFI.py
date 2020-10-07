from .Protocol import Protocol

class WF(Protocol):
    def __init__(self):
        self.category = 'WiFi'
        self.protocol = ['eth:ethertype:ip:tcp',
            'eth:ethertype:ip:tcp:tls']
        self.flags = None
        self.ipmap = None
        self.tcp = []
        self.package = []

    def load(self, filelist):
        self.load_packets(filelist[0:2])
        self.flags = self.load_data(filelist[2])
        self.ipmap = self.load_data(filelist[3])

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
        src = self.match_name(packet['ip']['ip.src_host'])
        srcIP = packet['ip']['ip.src']
        dst = self.match_name(packet['ip']['ip.dst_host'])
        dstIP = packet['ip']['ip.dst']
        seq = packet['tcp']['tcp.seq']
        nxtseq = packet['tcp']['tcp.nxtseq']
        info = packet['csv']['info']
        description = '<b>Frame No.</b> {}<br><b>Arrived at</b> {}<br><b>Source:</b> {} ({})\t\t<b>Destination:</b> {} ({}) \
        <br><b>Sequence:</b> {}\t\t<b>Next Sequence:</b> {}<br><b>Info:</b> {}'.format(num, time, src, srcIP, dst, dstIP, seq, nxtseq, info)
        return description

    def match_name(self, ip_string):
        for ip in self.ipmap:
            if ip['IP'] == ip_string:
                return ip['Name']

        l = ip_string.split('.')
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