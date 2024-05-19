#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Abase class for other classes to inhert from, providing common attribute
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize the base model instance.
        """
        DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        else:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime
                    (value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str[value]
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        Return a string representation of the insatnce.
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
                )

    def save(self):
        """
        Update the public instance attributes
        'updated at' with the current datetime.
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary containing all/values of the instance's __dict__.
        Adds a key __class__ with the class name of the object
        Convert created_at and updated_at to ISO format strings.
        """
        result_dict = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                result_dict[key] = value
            else:
                result_dict[key] = self.__class__.__name__
        return result_dict
