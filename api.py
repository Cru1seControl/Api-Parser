# -*- coding: utf-8 -*-
"""Api-Parser Documentation\n
Api-Parser is a simple tool used for the manipulation and
easy reading of json data returned from an api. Api also has the
ability to host a light socket server from where json data can be pulled from.

Basic usage:
    >>> from api import *
    >>> url = "https://www.blockchain.com/ticker"
    >>> print(apiKeys(apiDoc(url), True, sep=", "))
    USD, AUD, BRL, CAD, CHF, CLP, CNY, DKK, EUR, GBP (etc.)
"""

import requests
import socket
import json

__author__ = "Cru1seControl"
__version__ = 1.2

def apiKeys(obj, stringify=False, records=False, sep=None):
    """
apiKeys can be called with 3 parameters. Stringify converts the keys list to a string. Records can convert the list to a json dictionary with json.loads & cannot be used with stringify or sep.

Args:
    obj (func): 1st, Required parameter.
    stringify (bool): 2nd, Optional parameter. 
    records (bool): 3rd, Optional parameter.
    sep (null/bool): 4th, Optional parameter

Basic usage:
    >>> from api import *
    >>> doc = apiDoc("https://api-page.com")
    >>> print(apiKeys(doc))
    """
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
    """
apiDoc is the base function for apiKeys & apiIndex. Parameter url sets api page. Parameter key optionaly can be set for user/password for api page otherwise None.

Args:
    url (str): 1st, Required parameter.
    key (null/bool): 2nd, Optional parameter.

Basic usage:
    >>> from api import *
    >>> doc = apiDoc("https://api-page.com")
    >>> print(doc)
    """
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
    """
apiIndex is used to "index" an api document. Parameter *args are arguments supplied. Parameter indexing is secondary index for json lists.


Args:
    obj (func): 1st, Required parameter.
    args (tuple): 2nd, Required parameter.
    indexing (null/bool): 3rd, Optional parameter.

Basic usage:
    >>> from api import *
    >>> doc = apiDoc("https://api-page.com")
    >>> index = apiIndex(doc, "name1", "name2")
    >>> print(index)

    """
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
    """
apiFile returns an object containing json data from a file. 

Args:
    filename (str): 1st, Required parameter.

Basic usage:
    >>> from api import *
    >>> print(apiFile("api-example.json"))
    """
    try:
        with open(filename, "r") as fileout: #read and return json data from file
            json_data = json.loads(fileout.read())
            return json_data
    
    except Exception as fileerror:
        print(fileerror)

def apiConv(dictionary, writeout=False, sort=True, indent=4):
    """
apiConv converts raw dict into a json dictionary. Parameter dictionary is the dict to be loaded. Parameter writeout will write to a file named "json-output.json". Parameter sort will sort the dictionary. Parameter indent sets indentation for the json output.

Args:
    dictionary (dict): 1st, Required parameter.
    writeout (bool): 2nd, Optional parameter.
    sort (bool): 3rd, Optional parameter.
    indent (int): 4th, Optional parameter.

Basic usage:
     >>> from api import *
     >>> convert = apiConv({"example": {"key": 1}})
     >>> print(convert)
    """
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
    """
apiHost hosts a light socket server for a document. Parameter address sets the addr to be used, address:port in one string. Parameter document sets the json document from a file.

Args:
    address (str): 1st, Required parameter.
    document (str): 2nd, Required parameter.

Basic usage:
    >>> from api import *
    >>> apiHost("127.0.0.1:8080", "api-example.json")
    """
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
    """
apiHostconn is a client for apiHost. Parameter address sets the addr to connect to, address:port in one string. Parameter writeout optional argument for writing to a file named "json-output.json".

Args:
    address (str): 1st, Required parameter.
    writeout (bool): 2nd, Optional parameter.

Basic usage:
    >>> from api import *
    >>> apiHostconn("127.0.0.1:8080", True)
    """
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
