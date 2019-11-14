import requests
import pprint
import json

def apiParse(url, *args, keys=False):
    try:
        req = requests.get(url)
        api_page = req.content

        requested_api = json.loads(api_page)

        if keys == False:
        	pass
        else:
            print("Keys:", [key for key in requested_api.keys()])

        if not args:
            pprint.pprint(requested_api)
        else:
            pprint.pprint([requested_api[arguments] for arguments in args])

    except Exception as error:
        print(error)

def apifileParse(filename, arg=None, keys=False):
    try:
        with open(filename, "r") as filereader:
            json_data = json.loads(filereader.read())
            if keys == False:
                pass
            else:
                print("Keys:", json_data.keys())
            
            if not arg:
                pprint.pprint(json_data)
            else:
                pprint.pprint(json_data[arg])
            filereader.close()
    
    except Exception as fileerror:
        print(fileerror)
