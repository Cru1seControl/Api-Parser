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

def apiFile(filename, *args, indexing=None):
    with open(filename, "r") as fileout:
        json_data = json.loads(fileout.read())

        if args and indexing:
            return [json_data[arguments][indexing] for arguments in args]

        elif not args or indexing:
            return json_data
        else:
            return [json_data[arguments] for arguments in args]
