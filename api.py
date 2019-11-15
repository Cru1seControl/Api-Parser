import requests
import pprint
import json

def apiParse(url, *args, indexing=None, keys=False):
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

        elif indexing:
            pprint.pprint([requested_api[arguments][indexing] for arguments in args])

        else:
            pprint.pprint([requested_api[arguments] for arguments in args])

    except Exception as error:
        print(error)

def apifileParse(filename, *args, keys=False):
    try:
        with open(filename, "r") as filereader:
            json_data = json.loads(filereader.read())
            if keys == False:
                pass
            else:
                print("Keys:", [key for key in json_data.keys()])
            
            if not args:
                pprint.pprint(json_data)
            else:
                pprint.pprint([json_data[arguments] for arguments in args])
            filereader.close()
    
    except Exception as fileerror:
        print(fileerror)
