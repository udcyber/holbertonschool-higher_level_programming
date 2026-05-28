#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """Serialize the dictionary into XML and save it to the given filename"""
    root = ET.Element("data")
    for key, value in dictionary.items():
        elem = ET.SubElement(root, key)
        elem.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    """Read the XML data from the file, and return a deserialized 
    Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None


if __name__ == "__main__":

    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        serialize_to_xml(sample_dict, xml_file)
        print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        print(deserialized_data)

    if __name__ == "__main__":
        main()