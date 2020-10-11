from .FileIO import load_csv
from .FileIO import load_json

class Protocol(object):
    def __init__(self):
        self.category = 'Protocol'
        self.json_datas = None
        self.csv_datas = None

    def load_packets(self, filelist):
        self.json_datas = load_json(filelist[0])
        self.csv_datas = load_csv(filelist[1])

    def load_data(self, filename):
        return load_json(filename)

    def filter(self, protocol):
        packets = []
        for j in self.json_datas:
            packet = j['_source']['layers']
            if packet['frame']['frame.protocols'] in protocol:
                c = self.get_csv(packet['frame']['frame.number'])
                packet['csv'] = c
                packets.append(packet)
        return packets

    def get_csv(self, frame_num):
        dic = {}
        for c in self.csv_datas:
            if c['No.'] == frame_num:
                dic['src'] = c['Source'].split('_')[0]
                dic['arrival'] = c['Time']
                #dic['dst'] = c['Destination']
                dic['info'] = c['Info']
                break
        return dic

    def gather(self):
        pass

    def pack(self):
        pass

    def gen_description(self):
        pass

    def gen_color_key(self):
        pass