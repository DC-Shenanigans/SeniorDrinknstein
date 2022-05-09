import json

# In:   json file path
# Out:  Python object representing that json file
#       None if error
def load_from_json(json_file):
    try:
        with open(json_file, "r") as f:
            return json.loads(f.read())
    except:
        # TODO: check which display to write to
        print("Error reading/parsing '", json_file, "'")
        return None