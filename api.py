import requests
import pprint
import json

def apiParse(url, arg=None, keys=False):
    try:
        req = requests.get(url)
        api_page = req.content

        requested_api = json.loads(api_page)

        if keys == False:
        	pass
        else:
            print("Keys:", requested_api.keys())

        if not arg:
            pprint.pprint(requested_api)
        else:
            pprint.pprint(requested_api[arg])

    except Exception as error:
        print(error)