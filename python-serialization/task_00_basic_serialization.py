import json

def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python Dictionary to a JSONfile.

    Parameters:
        data: A Python Dictionary with data.
        filename: The filename of the output JSON file.
    """
    with open(filename, "w") as my_file:
        json.dump(data, my_file)

def load_and_deserialize(filename):
    """
    Deserialize the JSON file to recreate the Python Dictionary.

    Parameters:
        filename: The filename of the input JSON file.
    Return:
        A Pyton Dictionary with the deserialized JSON data from the file.
    """
    with open(filename, "r") as my_file:
        return json.load(my_file)
