import json
import csv

def load_csv(filename):
    f = open(filename)
    reader = csv.DictReader(f)
    data = []
    for line in reader:
        data.append(line)
    return data

def load_json(filename):
    #print(filename)
    #f = open(filename)
    #f = open(filename, encoding='unicode_escape')
    f = open(filename, encoding='UTF8')
    data = json.load(f)
    f.close()
    return data

def store_json(filename, data):
    f = open(filename, 'w')
    data = json.dump(data, f, indent=4)
    f.close()
    return True