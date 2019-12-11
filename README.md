# Api-Parser
*Simple API parser written in python*

*apiDoc*, *apiFile* *apiHostconn* & *apiConv* are your base handlers for all operations. The examples below show these functions, make a new Document and then apply one of the other objects such as *apiKeys* or *apiIndex* to the Document. Creating json tables can be done with *apiConv* and then can be exported to a local file or returned as a string.

# Dependencies
```
import requests
import socket
import json
```

# Examples

**Document and key printing**
- Document = apiDoc("https://blockchain.info/ticker")
- print(apiKeys(Document, stringify=True, sep=", "))

**Index of document**
- Document = apiDoc("https://blockchain.info/ticker")
- print(apiIndex(Document, "USD", indexing="15m"))

**Document with authentication**
- Document = apiDoc("https://api.exampledomain.com/", ("", "TOKEN"))
- print(apiKeys(Document, "Example", indexing="Author"))

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
$ python3 -c "from api import apiHost; apiHost('127.0.0.1:8080', 'api-example.json')"
```
**Retrieve Document**
- Document = apiHostconn("127.0.0.1:8080")
- print(apiIndex(Document, "Example", indexing="Email"))
```
$ curl 127.0.0.1:8080
```
