import requests
import xml.etree.ElementTree as ET
import re

# Setze deinen DeepL API-Schlüssel hier ein
DEEPL_API_KEY = ""

# URL für die DeepL API
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Funktion, um Text von Englisch nach Deutsch zu übersetzen
def translate_text(text):
    if text is None:
        return None
    
    # Extrahiere den Text innerhalb der geschweiften Klammern
    placeholders = re.findall(r'\{(.*?)\}', text)
    
    if placeholders:
        modified_text = text
        for idx, placeholder in enumerate(placeholders):
            modified_text = modified_text.replace("{" + placeholder + "}", f"{{{idx}}}")
        
        params = {
            "auth_key": DEEPL_API_KEY,
            "text": modified_text,
            "target_lang": "DE"
        }
        response = requests.get(DEEPL_API_URL, params=params)
        translation = response.json()["translations"][0]["text"]
        
        # Setze die Platzhalter an ihren ursprünglichen Platz
        for idx, placeholder in enumerate(placeholders):
            translation = translation.replace(f"{{{idx}}}", "{" + placeholder + "}")
    else:
        params = {
            "auth_key": DEEPL_API_KEY,
            "text": text,
            "target_lang": "DE"
        }
        response = requests.get(DEEPL_API_URL, params=params)
        translation = response.json()["translations"][0]["text"]
    
    return translation

# Pfad zur XML-Datei
xml_file_path = "english_help.xml"

# XML-Datei einlesen
tree = ET.parse(xml_file_path)
root = tree.getroot()

total_elements = 0
for element in root:
    total_elements += len(list(element.iter("Value")))
    total_elements += len(list(element.iter("Description")))
    total_elements += len(list(element.iter("Title")))
    total_elements += len(list(element.iter("Text")))
    total_elements += len(list(element.iter("String")))
    
translated_elements = 0

# Schleife über alle Wurzelelemente
for root_element in root:
    for idx, element in enumerate(root_element.iter("Value")):
        original_text = element.text
        translated_text = translate_text(original_text)
        element.text = translated_text
        translated_elements += 1
        progress = (translated_elements / total_elements) * 100
        print(f"Übersetze Element Value {translated_elements}/{total_elements} ({progress:.2f}% abgeschlossen)")

    for idx, element in enumerate(root_element.iter("Description")):
        original_text = element.text
        translated_text = translate_text(original_text)
        element.text = translated_text
        translated_elements += 1
        progress = (translated_elements / total_elements) * 100
        print(f"Übersetze Element Description {translated_elements}/{total_elements} ({progress:.2f}% abgeschlossen)")

    for idx, element in enumerate(root_element.iter("Title")):
        original_text = element.text
        translated_text = translate_text(original_text)
        element.text = translated_text
        translated_elements += 1
        progress = (translated_elements / total_elements) * 100
        print(f"Übersetze Element Title {translated_elements}/{total_elements} ({progress:.2f}% abgeschlossen)")

    for idx, element in enumerate(root_element.iter("Text")):
        original_text = element.text
        translated_text = translate_text(original_text)
        element.text = translated_text
        translated_elements += 1
        progress = (translated_elements / total_elements) * 100
        print(f"Übersetze Element Text {translated_elements}/{total_elements} ({progress:.2f}% abgeschlossen)")

    for idx, element in enumerate(root_element.iter("String")):
        original_text = element.text
        translated_text = translate_text(original_text)
        element.text = translated_text
        translated_elements += 1
        progress = (translated_elements / total_elements) * 100
        print(f"Übersetze Element Text {translated_elements}/{total_elements} ({progress:.2f}% abgeschlossen)")

# Übersetzte XML-Datei speichern
translated_xml_file_path = ""
tree.write(translated_xml_file_path, encoding="utf-8")

print("Übersetzung abgeschlossen. Übersetzte XML-Datei wurde gespeichert.")