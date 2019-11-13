# Api-Parser
*First program uploaded to github!*
Simple API parser written in python.

Usage
from api import *
Keys controls if you would like the dictionary keys to be printed
Arg controls what argument out of the dictionary to be printed otherwise None
Filename controls well the filename of the file you would like to parse

ONE LINERS

python3 -c "from api import *; apiParse('https://jsonplaceholder.typicode.com/todos/1', keys=True, arg='title')"
python3 -c "from api import *; apifileParse('filename.txt', keys=True, arg='title')"
