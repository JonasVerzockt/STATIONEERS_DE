import xml.etree.ElementTree as ET

input_file_path = 'german.xml'
output_file_path = 'ausgabe.txt'


tree = ET.parse(input_file_path)

key_value_pairs = []

for record in tree.findall('.//RecordThing') + tree.findall('.//Record'):
    key_element = record.find('Key')
    value_element = record.find('Value')
    
    if key_element is not None and value_element is not None:
        key = key_element.text
        value = value_element.text
        key_value_pairs.append((key, value))

key_value_pairs.sort(key=lambda x: x[0])

with open(output_file_path, 'w') as output_file:
    for key, value in key_value_pairs:
        output_file.write(f"Key: {key}, Value: {value}\n")

print("Sortierte Key-Value-Paare wurden in die Ausgabedatei geschrieben.")