import argparse
import json
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key',
    action="store", dest="key",
    help="Key string", required=True)
parser.add_argument('-v', '--value',
    action="store", dest="value",
    help="Value string")
parser.add_argument("-d", "--dir",  dest="path",
    help="path to search for jsons", default=os.getcwd())

args = parser.parse_args()

def flatten_json(json_str):
    out = {}
    
    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(json_str)
    return out

def check_key(key_check,dict):
    result = {}
    for key, value in dict.items():
        parts = key.split("_")
        if key_check in parts:
            result[key] = value
    return result

def check_value(value_check,dict):
    result = {}
    for key, value in dict.items():
        if value == value_check:
            result[key] = value
    return result

def inspect_file(file_path):
    str = open(file_path, 'r').read()
    obj = flatten_json(json.loads(str))
    
    filtered = check_key(args.key,obj)
    if args.value:
        filtered = check_value(args.value,filtered)
    return filtered

def pretty_print(data):
    for key, value in data.items():
        print("Found in file {}:".format(key))
        try:
            for k,v in value.items():
                print("Key: {}, Value: {}".format(k,v))
            print("\n")
        except:
            print("This was unexpected")
            pass

def main():
    data = {}
    files_in_dir = [f for f in os.listdir(args.path) if os.path.isfile(f)]
    for file in files_in_dir:
        if file.endswith((".json")):
                found = inspect_file(os.path.join(args.path,file))
                if found:
                    data[file] = found
    if data:
        pretty_print(data)
    else:
        print("Nothing found.")


if __name__ == "__main__":
    main()
