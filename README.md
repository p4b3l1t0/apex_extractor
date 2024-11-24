# Apex and Aura Controller Extractor

This tool is designed to extract Salesforce Apex and Aura Controllers from a JavaScript file, typically named `app.js`, used in Salesforce Lightning applications.

## Description

The script utilizes regular expressions to search for patterns indicating Apex and Aura Controllers in the JavaScript file. It extracts these controllers and saves them in a text file named `object.txt`.

## Requirements

- Python 3
- A JavaScript file (commonly `app.js`) from a Salesforce Lightning application

## Usage

1. Clone this repository or copy the script.
2. Place your JavaScript file in the same directory as the script or specify the path.
3. Run the script using Python 3:

`python3 extract.py <path_to_your_app.js_file>` 

Replace `<path_to_your_app.js_file>` with the path to your JavaScript file.

The script will create object.txt and api.txt files. The object.txt file contains the extracted controllers, and the api.txt file contains the extracted API names.

### BurpSuite Steps

To use the extracted controllers with BurpSuite for fuzzing or testing, follow these steps:

1. Send any POST request with an Aura endpoint to BurpSuite's Repeater.

2. Replace the `message` parameter in your request with the following payload:

```{"actions":[{"id":"1;a","descriptor":"aura://ListUiController/ACTION$getListsByObjectName","callingDescriptor":"UHNKNOWN","params":{"objectApiName":"***"}}]}```

3. In Intruder, choose *** in the params (objectApiName, entityNameOrId) as the position.

4. Let the "payload type" remain as "Simple List".

5. Upload the object.txt and api.txt files or paste the lists into “payload options”.

6. Run the Intruder attack for all objects and API names whenever possible, both as a guest user and as different authenticated users, to understand different permissions.

5. Upload the object.txt file or paste the objects list into “payload options”.

6. Run the Intruder attack for all objects whenever possible, both as a guest user and as different authenticated users, to understand different permissions.
