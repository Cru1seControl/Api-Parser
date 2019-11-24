# Api-Parser
*Simple API parser written in python*

Usage

*apiDoc* and *apiFile* are your base handlers for all operations. The examples below show this function, make a new Document and then apply one of the other objects such as *apiKeys* to the Document. Creating json tables can be done with *apiConv* and then can be exported to a local file or printed as a string.

# Dependencies
```
import requests
import socket
import json
```

# Examples
from api import *

**Document and key printing**
- Document = apiDoc("https://blockchain.info/ticker")
- print(apiKeys(Document))

**Index of document**
- Document = apiDoc("https://blockchain.info/ticker")
- print(apiIndex(Document, "USD", indexing="15m"))

**Document file parsing**
- Document = apiFile("api-example.json")
- print(apiFile(Document, "Example", indexing="Email"))

**Json table conversion**
- Dictionary = {"Example": {"Author": "Cru1seControl", "Email": "Cru1seControl.loot@gmail.com"}}
- apiConv(Dictionary, writeout=True, sort=True, indent=4)

# Experimental Functions

**Host document**
- apiHost("127.0.0.1", 8080, "api-example.json")
```
$ curl http://127.0.0.1:8080/
```
