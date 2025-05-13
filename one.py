import json

a = '''{
"aa": [
    {"a": "mohit", "b": "rohan", "c": "kumar", "f": "wineet"},
    {"q": "qq", "w": "ww", "e": "ee", "r": "rr"}
]
}'''

# Parsing the JSON string into a Python dictionary
data = json.loads(a)

# Printing the parsed data
print("hi sir")
print(data)

#Its the conversion of python string to json data type /dictionary
