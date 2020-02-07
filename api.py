import requests
import socket
import json

__author__ = "Cru1seControl"
__version__ = 1.2

def apiKeys(obj, stringify=False, records=False, sep=None):
    try:
        if stringify == True and sep: #string conversion with sep
            return f"{sep}".join(obj.keys())

        elif stringify == True: #string conversion
            return " ".join(obj.keys())
        elif records == True: #convert keys to dictionary & display with json.loads
            return json.loads('{"response": {"records": "%s", "objects": "%s"} }' % (len(obj.keys()), [key for key in obj.keys()]))
        else:
            return [key for key in obj.keys()]

    except Exception as keyserror:
        print(keyserror)

def apiDoc(url, key=None):
    try:
        if not key:        
            req = requests.get(url) #get url without key
        else:
            req = requests.get(url, auth=(key)) #get url with key
            
        api_page = req.content #get content & return requested_api with json.loads
        requested_api = json.loads(api_page)
        return requested_api

    except Exception as apiDocerror:
        print(apiDocerror)

def apiIndex(obj, *args, indexing=None):
    try:
        if indexing: #return indexing for arguments
            for arguments in args:
                return obj[arguments][indexing]
        else:
            for arguments in args: #return argument without index
                return obj[arguments]

    except Exception as apiIndexerror:
        print(apiIndexerror)

def apiFile(filename):
    try:
        with open(filename, "r") as fileout: #read and return json data from file
            json_data = json.loads(fileout.read())
            return json_data
    
    except Exception as fileerror:
        print(fileerror)

def apiConv(dictionary, writeout=False, sort=True, indent=4):
    try: #take raw dictionary & format with json.dumps 
        json_formatted = json.dumps(dictionary, sort_keys=sort, indent=indent)
        if writeout == False:

            return json_formatted
        else:
            with open("json-output.json", "w") as writeout: #output to a file
                writeout.write(json_formatted)
                writeout.close()

    except Exception as apiConverror:
        print(apiConverror)

def apiHost(address, document):
    try:
        addr = address.split(":") #create server and host document locally/public
        sockObj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockObj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        sockObj.bind((addr[0], int(addr[1])))
        sockObj.listen(3)

        while True:
            client, addr = sockObj.accept()
            print(addr[0], addr[1])
            data = client.recv(10)
            with open(document, "r") as index:
                info = index.read()
                client.send(info.encode("ascii"))

        client.close()

    except Exception as apiHosterror:
        print(apiHosterror)
        
def apiHostconn(address, writeout=False):
    try:
        addrs = address.split(":") #connect to created server or just use curl/wget
        sockCli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockCli.connect((addrs[0], int(addrs[1])))

        sockCli.send(b"0")
        data = sockCli.recv(4096)

        if writeout == False:
            new_data = data.decode("utf-8").replace("\n", "")
            return json.loads(new_data.replace("    ", " "))

        else:
            with open("json-output.json", "w") as writeout:
                writeout.write(data.decode("utf-8"))
                writeout.close()

    except Exception as apiHostconnerror:
        print(apiHostconnerror)
