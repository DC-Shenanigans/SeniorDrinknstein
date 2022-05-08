import json

def read_drinks(drinks_json_file):
    try:
        drinks_json = open(drinks_json_file, "r")
        return json.loads(drinks_json)
    except:
        # TODO: to display
        print("File load/parse error")
        return None
