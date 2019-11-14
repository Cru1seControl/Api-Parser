# Api-Parser
*First program uploaded to github!*
Simple API parser written in python.

Usage

from api import *,
Keys controls if you would like the dictionary keys to be printed,
Args controls what arguments out of the dictionary to be printed otherwise All,
Filename "for apifileParse" controls well the filename of the file you would like to parse.

COPY PASTA

python3 -c "from api import *; apiParse('https://jsonplaceholder.typicode.com/todos/1', "title", "id", "completed", keys=True)"

python3 -c "from api import *; apifileParse('filename.txt', keys=True, arg='title')"
