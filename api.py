import requests
import socket
import json

__author__ = "Cru1seControl"
__version__ = 1.5

def apiKeys(obj):
    try:
        return obj.keys()

    except Exception as keyserror:
        print(keyserror)

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
            for arguments in args:
                return obj[arguments][indexing]
        else:
            for arguments in args:
                return obj[arguments]

    except Exception as apiIndexerror:
        print(apiIndexerror)

def apiFile(filename):
    try:
        with open(filename, "r") as fileout:
            json_data = json.loads(fileout.read())

            return json_data
    
    except Exception as fileerror:
        print(fileerror)

def apiConv(dictionary, writeout=False, sort=True, indent=4):
    try:
        json_formatted = json.dumps(dictionary, sort_keys=sort, indent=indent)
        if writeout == False:

            return json_formatted
        else:
            with open("json-output.json", "w") as writeout:
                writeout.write(json_formatted)
                writeout.close()

    except Exception as apiConverror:
        print(apiConverror)

def apiHost(address, port, document):
    sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockObj.bind((address, port))
    sockObj.listen(10)

    while True:
        client, addr = sockObj.accept()
        data = client.recv(4096)
        with open(document, "r") as index:
            info = index.read()
            client.send(b"HTTP/1.0 200 OK\r\n\r\n")
            client.send(info.encode("ascii"))

        print(addr[0], addr[1])

    client.close()