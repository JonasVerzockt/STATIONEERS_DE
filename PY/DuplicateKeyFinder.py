import xml.etree.ElementTree as ET

def find_duplicate_keys(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    key_dict = {}
    duplicate_keys = {}

    for idx, elem in enumerate(root.iter('Key'), start=1):
        key_value = elem.text.strip()
        if key_value in key_dict:
            if key_value not in duplicate_keys:
                duplicate_keys[key_value] = [key_dict[key_value], idx]
            else:
                duplicate_keys[key_value].append(idx)
        else:
            key_dict[key_value] = idx

    return duplicate_keys

def main():
    original_file = 'german.xml'
    duplicate_key_dict = find_duplicate_keys(original_file)

    if duplicate_key_dict:
        with open('doppelte_keys.txt', 'w') as output_file:
            output_file.write("Doppelte Keys gefunden:\n")
            for key, line_numbers in duplicate_key_dict.items():
                original_line = line_numbers[0]
                duplicate_lines = ", ".join(map(str, line_numbers[1:]))
                output_file.write(f"Key: {key}, Erste Zeilennummer: {original_line}, Doppelte Zeilennummern: {duplicate_lines}\n")
        print("Doppelte Keys wurden in 'doppelte_keys.txt' geschrieben.")
    else:
        print("Keine doppelten Keys gefunden.")

if __name__ == "__main__":
    main()