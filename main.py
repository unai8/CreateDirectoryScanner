import os
import json
from datetime import datetime

def get_directory_structure(rootdir):
    """
    Recorre recursivamente una carpeta y devuelve su estructura en un diccionario.
    """
    structure = {}
    for entry in os.scandir(rootdir):
        if entry.is_file():
            # Si es un archivo, almacenamos la información solicitada
            structure[entry.name] = {
                "name": entry.name,
                "path": entry.path,
                "is_file": True,
                "created": datetime.fromtimestamp(entry.stat().st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                "modified": datetime.fromtimestamp(entry.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
            }
        elif entry.is_dir():
            # Si es una carpeta, la recorremos recursivamente y almacenamos su estructura
            structure[entry.name] = {
                "name": entry.name,
                "path": entry.path,
                "is_file": False,
                "content": get_directory_structure(entry.path)
            }
    return structure

def write_to_json(structure, filepath):
    """
    Escribe la estructura de directorios en un archivo JSON en la ubicación especificada.
    """
    with open(filepath, "w") as f:
        json.dump(structure, f, indent=4)

# Ejemplo de uso
rootdir = "C:\\Users\\Unai\\Documents\\WebPage\\Michelin-WebPage"
structure = get_directory_structure(rootdir)
filename = "output.json"
filepath = os.path.join(os.getcwd(), filename)
write_to_json(structure, filepath)
