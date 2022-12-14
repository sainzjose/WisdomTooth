import os
import hashlib
from glob import glob


def get_bin_files():
    files = os.listdir("/usr/bin")
    for name in files:
        file_type = os.popen(f"file /usr/bin/{name}").read()
        file_data = file_type.split(" ")
        if file_data[1] not in "ELF":
            files.remove(name)
    
    for i in range(len(files)):
        files[i] = f"/usr/bin/{files[i]}"
    return files

def get_hash(files):
    hashes = list(tuple())
    for i in range(len(files)):
        path = f"/usr/bin/{files[i]}"
        hashes.append((path, hashlib.sha256(path.encode('utf-8')).hexdigest()))
    return hashes

def get_json():
    pass

files = get_bin_files()
print(get_hash(files))
#print(convert_to_hash(files))



