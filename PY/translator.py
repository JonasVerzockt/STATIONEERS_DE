import requests
import xml.etree.ElementTree as ET
import re

# Setze deinen DeepL API-Schlüssel hier ein
DEEPL_API_KEY = "TOKEN"

# URL für die DeepL API
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Funktion, um Text von Englisch nach Deutsch zu übersetzen
def translate_text(text):
    # Extrahiere den Text innerhalb der geschweiften Klammern
    placeholders = re.findall(r'\{(.*?)\}', text)
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
    
    return translation

# Pfade zur XML-Datei
xml_file_path = "english.xml"

# XML-Datei einlesen
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Schleife über alle Elemente mit den Tags "Value" und "Description"
for element in root.iter("Value"):
    original_text = element.text
    translated_text = translate_text(original_text)
    element.text = translated_text

for element in root.iter("Description"):
    original_text = element.text
    translated_text = translate_text(original_text)
    element.text = translated_text

# Übersetzte XML-Datei speichern
translated_xml_file_path = "german.xml"
tree.write(translated_xml_file_path, encoding="utf-8")

print("Übersetzung abgeschlossen. Übersetzte XML-Datei wurde gespeichert.")