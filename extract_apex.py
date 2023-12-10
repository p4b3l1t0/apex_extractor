import re

def extract_controllers(file_path):
    # Regular expression pattern to match aura:// and apex:// patterns
    pattern = r'(aura://[\w.\/$]+|apex://[\w.\/$]+)'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find all matches
        matches = re.findall(pattern, content)

        return matches
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Usage example
file_path = 'app.js'  # Replace with the path to your app.js file
controllers = extract_controllers(file_path)

# Write to object.txt
with open('object.txt', 'w', encoding='utf-8') as output_file:
    for controller in controllers:
        output_file.write(controller + '\n')
