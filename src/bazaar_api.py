import requests
import json 

""" Every sample in MalwareBazaar container the following fieds

1. Date        (date uploaded)
2. SHA256 Hash (unique identifier)
3. Type        (exe, elf, dll)
4. Signature   (malware signature, sometimes None)
5. Tag         (type, malware type, targetted architecture, etc...)
6. Report      (user who submitted sample)

"""

class MalwareBazaar:

    @staticmethod
    def get_samples_by_tag(file_type,number):
        """ Get X number of samples with a file type of Y. Returns a list of hashes.

        Only 1000 samples can be queryed at once
        Request will timeout in 15 seconds
        
        """

        if isinstance(file_type,str) is False or isinstance(number,str) is False:
            raise Exception("Invalid input type. Both inputs must be a string")
        data = {
            'query':'get_file_type',
            'file_type' :file_type,
            'limit':number,
        }
        response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=25)
        json_response = json.loads(response.text)
        return [item for item in json_response['data']]

    @staticmethod
    def download_file(hash):
        """ Expects a hash. Output dir is '../bin/malicious/hash' 
        """

        if isinstance(hash,str) is False:
            raise Exception("Invalid input type. Input must be a hash represented with a string")
        data = {
            'query':'get_file',
            'sha256_hash':hash
        }
        response = requests.post('https://mb-api.abuse.ch/api/v1/', data=data, timeout=100, allow_redirects=True)
        open(f"../bin/malicious/{hash}", 'wb').write(response.content)


# How to download 5 malicious elf files
# hashes = MalwareBazaar.get_samples_by_tag('elf','5')
# MalwareBazaar.download_files(hashes)