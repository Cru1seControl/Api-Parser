# Api-Parser
*Simple API parser written in python*

Usage

from api import *,
Keys controls if you would like the dictionary keys to be printed,
Args controls what arguments out of the dictionary to be printed otherwise All,
Indexing allows you to access dictionaries inside dictionaries for better parsing,
Filename "for apifileParse" controls the filename of the file you would like to parse.

COPY PASTA

python3 -c "from api import *; apiParse('https://jsonplaceholder.typicode.com/todos/1', 'title', 'id', 'completed', keys=True)"

python3 -c "from api import *; apiParse('https://blockchain.info/ticker', 'USD', 'AUD', indexing='15m', keys=True)"

python3 -c "from api import *; apifileParse('filename.txt', 'title', 'id', 'completed', keys=True)"
