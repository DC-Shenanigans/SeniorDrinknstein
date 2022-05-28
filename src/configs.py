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

# Makes sure ingredients are available
# In:   Configs as python objects
# Out:  True if good, False if not (fatal error)


def validate_config(pumps_config, drinks_config):
    avail_ing = []
    try:
        for p in pumps_config:
            avail_ing.append(p["ing"])
        for d in drinks_config:
            for i in d["ingredients"].keys():
                if (i not in avail_ing):
                    print("Error: Ingredients missing")
                    return False
        return True
    except:
        # TODO: check which display to write to
        print("Error: Invalid Config")
        return False
