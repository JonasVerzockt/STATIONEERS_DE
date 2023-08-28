def extract_keys(filename):
    with open(filename, 'r') as file:
        content = file.read()
        keys = []
        start_tag = "<Key>"
        end_tag = "</Key>"
        start_idx = content.find(start_tag)
        
        while start_idx != -1:
            end_idx = content.find(end_tag, start_idx)
            if end_idx != -1:
                key = content[start_idx + len(start_tag):end_idx].strip()
                keys.append(key)
                start_idx = content.find(start_tag, end_idx)
            else:
                break
    return keys

def main():
    file1_name = "english.xml"
    file2_name = "german.xml"

    keys_file1 = extract_keys(file1_name)
    keys_file2 = extract_keys(file2_name)

    missing_keys = set(keys_file1) - set(keys_file2)
    
    for key in missing_keys:
        print(f"<Key>{key}</Key>")

if __name__ == "__main__":
    main()