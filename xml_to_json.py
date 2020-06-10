from xml.dom.minidom import parseString

import dicttoxml
import xmltodict
import json


source = 'source.xml'
result = 'result.json'
reverse = 'reverse.xml'

with open(source, 'r') as f:
    doc = xmltodict.parse(f.read())
with open(result, 'w') as f:
    json.dump(doc, f, ensure_ascii=False, indent=4)

# import pprint
# pp.pprint(json.dumps(doc))
# pp = pprint.PrettyPrinter(indent=4)

with open(result, 'r') as f:
    doc = json.loads(f.read())

pretty = parseString(dicttoxml.dicttoxml(doc, root=False, attr_type=False))

with open(reverse, 'w') as f:
    f.write(pretty.toprettyxml(indent=' '*4))

