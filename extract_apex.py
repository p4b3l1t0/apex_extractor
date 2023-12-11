import re
import json

def extract_controllers_and_api_names(file_path):
    # Regular expression pattern to match aura:// and apex:// patterns
    controller_pattern = r'(aura://[\w.\/$]+|apex://[\w.\/$]+)'
    # Regular expression pattern to extract 'name' values within the JSON structure
    api_name_pattern = r'\"name\":\"([^\"]+)\"'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Find all controller matches
        controller_matches = re.findall(controller_pattern, content)
        # Find all API name matches
        api_name_matches = re.findall(api_name_pattern, content)

        return controller_matches, api_name_matches
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []

# Usage example
file_path = 'app.js'  # Replace with the path to your app.js file
controllers, api_names = extract_controllers_and_api_names(file_path)

# Write to object.txt and api.txt
with open('object.txt', 'w', encoding='utf-8') as object_file, \
     open('api.txt', 'w', encoding='utf-8') as api_file:
    for controller in controllers:
        object_file.write(controller + '\n')
    for api_name in api_names:
        api_file.write(api_name + '\n')
