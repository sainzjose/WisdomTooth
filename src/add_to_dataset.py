from bazaar_api import MalwareBazaar
import radare_extraction
import subprocess
import json 

TAG = 'elf'
SAMPLES = '1000'
JSON = 'malicious_dataset.json'

samples = MalwareBazaar.get_samples_by_tag(TAG,SAMPLES)

for sample in samples:
    hash = sample['sha256_hash']
    sample_path = f"../bin/malicious/{hash}"
    
    MalwareBazaar.download_file(hash)
    subprocess.call(["7z", "x", "-pinfected", sample_path])
    json_cfg = radare_extraction.extract_json_cfg(f"./{hash}.elf")
    
    with open(JSON,'r') as file:
        json_file = json.load(file)
    
    json_file[sample['sha256_hash']] = json_cfg
    
    with open(JSON, "w") as file:
        json.dump(json_file, file)

    subprocess.call(["rm", f"{hash}.elf"])