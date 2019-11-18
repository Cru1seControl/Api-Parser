import requests
import json

__author__ = "Cru1seControl"
__version__ = 1.4

def apiKeys(obj):
    try:
        return obj.keys()

    except Exception:
        return obj[0].keys()

def apiDoc(url):
    try:
        req = requests.get(url)
        api_page = req.content
        requested_api = json.loads(api_page)

        return requested_api

    except Exception as apiDocerror:
        print(apiDocerror)

def apiIndex(obj, *args, indexing=None):
    try:

        if indexing:

            return [obj[arguments][indexing] for arguments in args]
        else:
            return [obj[arguments] for arguments in args]

    except Exception as apiIndexerror:
        print(apiIndexerror)

def apiFile(filename):
    try:
        with open(filename, "r") as fileout:
            json_data = json.loads(fileout.read())

            return json_data
    
    except Exception as fileerror:
        print(fileerror)

def apiConv(dictionary, sort=True, indent=4):
    try:
        json_encoded = json.dumps(dictionary, sort_keys=sort, indent=indent)
        return json_encoded

    except Exception as apiConverror:
        print(apiConverror)
