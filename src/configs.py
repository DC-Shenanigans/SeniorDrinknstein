import json

# In:   json file path
# Out:  Python object representing that json file
#       None if error
def load_from_json(json_file):
    try:
        f = open(json_file, "r")
        return json.loads(f.read())
    except:
        # TODO: check which display to write to
        print("File load/parse error")
        return None
    finally:
        f.close()
    
