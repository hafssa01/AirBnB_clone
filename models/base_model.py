#!/usr/bin/python3
"""
This is the BaseModel class
that contains the basic attributes
and methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        """
        Returns a dictionary representation of the instance
        """
        inst_dict = self.__dict__.copy()
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        inst_dict["__class__"] = self.__class__.__name__
        return inst_dict


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]))
