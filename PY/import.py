import xml.etree.ElementTree as ET

# Lese die XML-Datei ein
xml_tree = ET.parse('german.xml')
root = xml_tree.getroot()

# Lese die TXT-Datei im ANSI-Format ein
with open('ausgabe.txt', 'r', encoding='ansi') as txt_file:
    lines = txt_file.readlines()

# Initialisiere Variablen für Key und Value
current_key = None
current_value = None

# Iteriere durch die Zeilen der TXT-Datei
for line in lines:
    # Teile die Zeile an ";" auf
    parts = line.strip().split('; ')
    
    if len(parts) == 4 and parts[0] == 'Key' and parts[2] == 'Value':
        # Wenn die Zeile den Key und Value enthält
        current_key = parts[1]
        current_value = parts[3]
    elif current_key is not None and current_value is not None:
        # Wenn Zeilenumbrüche im aktuellen Value auftreten, füge sie hinzu
        current_value += '\n' + line.strip()
    else:
        # Wenn die Zeile nicht erwartet wird, überspringe sie
        continue
    
    # Suche nach dem entsprechenden Element im XML
    for element in root.findall(".//*[Key='" + current_key + "']"):
        element.find('Value').text = current_value

# Speichere die aktualisierte XML-Datei
xml_tree.write('aktualisierte_xml_datei.xml', encoding='utf-8')