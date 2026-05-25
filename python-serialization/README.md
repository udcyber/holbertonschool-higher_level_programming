# Python - Serialization
---
## 0. Basic Serialization

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

Instructions:  
Write a Python module named ```task_00_basic_serialization.py``` with the following functions:
```
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```
The function ```serialize_and_save_to_file``` takes 2 parameters:

- ```data```: A Python Dictionary with data
- ```filename```: The filename of the output JSON file. If the output file already exists it should be replaced.
  
The function ```load_and_deserialize``` take 1 ```parameters```:

- ```filename```: The filename of the input JSON file This function returns a Python Dictionary with the deserialized JSON data from the file.
  
Execution Output Example:
```
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')

# Output: The data has been serialized and saved to 'data.json'
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')

# Output: The deserialized data
print("Deserialized Data:")
print(deserialized_data)
```
```
Data serialized and saved to 'data.json'.
Deserialized Data:
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```
  
Repo:  
  
GitHub repository: holbertonschool-higher_level_programming  
Directory: python-serialization  
File: task_00_basic_serialization.py  
  
---

1. Pickling Custom Classes

Learn how to serialize and deserialize custom Python objects using the ```pickle``` module.
  
Instructions:
1 - Create a custom Python class named CustomObject. This class should have the following attributes:

name (a string)

age (an integer)

is_student (a boolean)

Additionally, the class should have a method display method to print out the object's attributes with the following format:
