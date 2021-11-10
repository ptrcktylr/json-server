import json
import random

# list of names to add to addresses
names = ['United States Postal Service', 'Rush My Passport', 'Express Passport', 'Fastport Passport', 'Walgreens Photo', 'US Passport Office', 'ItsEasy Passport & Visa']

# read old file
with open('old_db.json', 'r') as f:
    data = json.load(f)
    # for each address add a name field
    for address_obj in data['addresses']:
        address_obj['name'] = random.choice(names)
    # write to new file
    with open('db.json', 'w') as new_f:
        json.dump(data, new_f, indent=4)