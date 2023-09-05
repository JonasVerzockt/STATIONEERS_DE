def find_duplicate_prefixes(file_path):
    prefixes = {}  # Ein Wörterbuch, um die Zeilen mit doppelten Präfixen zu speichern
    line_number = 0

    with open(file_path, 'r') as file:
        for line in file:
            line_number += 1
            line = line.strip()  # Leerzeichen am Anfang und Ende der Zeile entfernen

            # Den Teil nach dem Key: extrahieren
            parts = line.split("Key: ")
            if len(parts) != 2:
                # Wenn die Zeile kein 'Key:' enthält, überspringe sie stillschweigend
                continue

            prefix = parts[1]

            if prefix in prefixes:
                # Wenn das Präfix bereits gesehen wurde, füge die Zeile zur Liste hinzu
                prefixes[prefix].append(line_number)
            else:
                # Andernfalls erstelle eine neue Liste für dieses Präfix
                prefixes[prefix] = [line_number]

    # Durchlaufe das Wörterbuch und zeige Zeilen mit doppelten Präfixen an
    for prefix, line_numbers in prefixes.items():
        if len(line_numbers) > 1:
            print(f"Doppelter Anfang '{prefix}' in Zeilen: {', '.join(map(str, line_numbers))}")

if __name__ == "__main__":
    file_path = "ausgabe.txt"  # Passe den Dateipfad an
    find_duplicate_prefixes(file_path)