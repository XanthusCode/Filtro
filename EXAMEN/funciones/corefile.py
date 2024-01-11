import os
import json

RUTA = ''

def save_file(*param):
    with open(RUTA, 'w') as wf:
        json.dump(param[0],wf,indent=4)

def open_file():
     with open(RUTA, 'r') as rf:
        json.load(rf)

def eliminar(param, index_to_remove):
    new_data = param.pop(index_to_remove)
    return new_data

def check_file(*param):
    if (os.path.isfile(RUTA)):
        file_data = open_file()
    else:
        if(len(param) > 0):
            save_file(param)

            