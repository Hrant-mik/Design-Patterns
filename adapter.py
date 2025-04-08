import xmltodict
import json



xml_data = """
<person>
    <name>John</name>
    <age>30</age>
    <city>New York</city>
</person>
"""

class Adapter:
    def xml_to_json(self, xml):
        dict_data = xmltodict.parse(xml)
        return json.dumps(dict_data, indent=4)
    
    


adapter = Adapter()
print(adapter.xml_to_json(xml_data))