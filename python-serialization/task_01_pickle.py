#!/usr/bin/env python3

import pickle


class CustomObject:
    """Custom class CustomObject.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print out the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance of the object and save it to
        the provided filename."""
        try:
            with open(filename, "wb") as my_file:
                pickle.dump(self, my_file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """Loads and returns an instance of the CustomObject from the
        provided filename"""
        try:
            with open(filename, "rb") as my_file:
                return pickle.load(my_file)
        except Exception:
            return None


# main to test
if __name__ == "__main__":

    # Create an instance of CustomObject
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()

    # Serialize the object
    obj.serialize("object.pkl")

    # Deserialize the object into a new instance
    new_obj = CustomObject.deserialize("object.pkl")
    print("\nDeserialized Object:")
    new_obj.display()
