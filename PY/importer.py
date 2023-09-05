import xml.etree.ElementTree as ET

# Öffne die XML-Datei und lese sie ein
xml_tree = ET.parse('C:\\Users\\Jonas\\Documents\\GitHub\\STATIONEERS_DE\\DE_DeepL\\german.xml')
xml_root = xml_tree.getroot()

# Erstelle ein Dictionary, um die Key-Value-Paare aus der TXT-Datei zu speichern
txt_data = {}

# Lese die TXT-Datei und speichere die Key-Value-Paare im Dictionary
with open('C:\\Users\\Jonas\\Documents\\GitHub\\STATIONEERS_DE\\DE_DeepL\\ausgabe.txt', 'r', encoding='iso-8859-1') as txt_file:
    current_key = None
    current_value = None
    for line in txt_file:
        if line.startswith('Key: '):
            current_key = line.strip()[4:]
        elif line.startswith('Value: '):
            current_value = line.strip()[6:]
            if current_key:
                txt_data[current_key] = current_value

# Iteriere durch die XML-Elemente und aktualisiere die Werte entsprechend den Szenarien
for element in xml_root.findall('.//*'):
    key_element = element.find('Key')
    if key_element is not None:
        key = key_element.text
        if key in txt_data:
            element.find('Value').text = txt_data[key]
            del txt_data[key]

# Füge fehlende Key-Value-Paare aus der TXT-Datei hinzu
for key, value in txt_data.items():
    new_element = ET.Element('Record')
    key_element = ET.Element('Key')
    key_element.text = key
    value_element = ET.Element('Value')
    value_element.text = value
    new_element.append(key_element)
    new_element.append(value_element)
    xml_root.append(new_element)

# Speichere die aktualisierte XML-Datei im UTF-8-Format
xml_tree.write('C:\\Users\\Jonas\\Documents\\GitHub\\STATIONEERS_DE\\DE_DeepL\\aktualisierte_xml_datei.xml', encoding='utf-8')