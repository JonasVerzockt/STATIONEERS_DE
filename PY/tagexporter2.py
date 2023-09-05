import xml.etree.ElementTree as ET

input_file_path = 'german.xml'
output_file_path = 'ausgabe.txt'

tree = ET.parse(input_file_path)

key_value_pairs = []

for record in tree.findall('.//RecordThing') + tree.findall('.//Record'):
    key_element = record.find('Key')
    description_element = record.find('Description')  # Änderung hier
    
    if key_element is not None and description_element is not None:  # Änderung hier
        key = key_element.text
        description = description_element.text  # Änderung hier
        key_value_pairs.append((key, description))  # Änderung hier

key_value_pairs.sort(key=lambda x: x[0])

with open(output_file_path, 'w') as output_file:
    for key, description in key_value_pairs:  # Änderung hier
        output_file.write(f"Key: {key}, Description: {description}\n")  # Änderung hier

print("Sortierte Key-Description-Paare wurden in die Ausgabedatei geschrieben.")  # Änderung hier