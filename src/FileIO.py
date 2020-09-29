import json
import csv

class IO:
    def __init__(self):
        pass

    def load_csv(self, filename):
        f = open(filename)
        reader = csv.DictReader(f)
        d = []
        for line in reader:
            d.append(line)
        return d

    def load_json(self, filename):
        f = open(filename)
        d = json.load(f)
        f.close()
        return d

    def store_json(self, filename, data):
        f = open(filename, 'w')
        d = json.dump(data, f, indent=4)
        f.close