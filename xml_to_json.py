import xmltodict
import json

source = 'source.xml'
result = 'result.json'

with open(source, 'r') as f:
    doc = xmltodict.parse(f.read())
with open(result, 'w') as f:
    json.dump(doc, f, ensure_ascii=False, indent=4)

# import pprint
# pp.pprint(json.dumps(doc))
# pp = pprint.PrettyPrinter(indent=4)
