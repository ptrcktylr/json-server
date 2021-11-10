import json

# read old file
with open('old_db.json', 'r') as f:
    data = json.load(f)
    # for each address add a name field
    for address_obj in data['addresses']:
        address_obj['name'] = "United States Postal Service"
    # write to new file
    with open('db.json', 'w') as new_f:
        json.dump(data, new_f, indent=4)