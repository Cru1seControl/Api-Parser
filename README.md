# Api-Parser
*Simple API parser written in python*

Usage

apiDoc and apiFile are your base handlers for all operations. The examples below show this function, make a new Document and then apply one of the other objects such as apiKeys to the Document.

# Examples
from api import *

#Document and key printing

Document = apiDoc("https://blockchain.info/ticker")

print(apiKeys(Document))

#Index of document

Document = apiDoc("https://blockchain.info/ticker")

print(apiIndex(Document, "USD", indexing="15m"))

#Document file parsing

Document = apiFile("api-example.json")

print(apiFile(Document, "Example", indexing="Email"))
