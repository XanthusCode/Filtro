import os
import json

RUTA = ''


def save_file(data):
    with open(RUTA, 'w') as wf:
        json.dump(data, wf, indent=4)

def open_file():
    with open(RUTA, 'r') as rf:
        return json.load(rf)

def eliminar(data, index_to_remove):
    if 0 <= index_to_remove < len(data):
        del data[index_to_remove]
    return data

def check_file(*param):
    if os.path.isfile(RUTA):
        file_data = open_file()
        return file_data
    else:
        if len(param) > 0:
            save_file(param[0])
            return param[0]
        else:
            return None