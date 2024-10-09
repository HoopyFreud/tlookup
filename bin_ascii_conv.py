import json
import base64

with open('jsonDB/cardTable.json', "rb") as fh:
    jsonObject = fh.read()
with open('jsonDB/cardTableOb', "w") as fh:
    print(base64.b64encode(jsonObject).decode('utf-8'))
    fh.write(base64.b64encode(jsonObject).decode('utf-8'))
with open('jsonDB/cardTableOb') as fh:
    print(json.loads(base64.b64decode(fh.read()).decode('utf-8')))