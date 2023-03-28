from models import storage
import uuid
# we have to import a uuid module so that we can assign uuid
from datetime import datetime

class BaseModel:
    """
    This is a class that defines all common attributes/ methods
    for other classes to inherit from
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        #we will return a string representation of the object which includes:
        #class name of the object: type(self).__name__
        #the id of the object: self.id
        #the attributes of the objects in a dictionary: self.__dict__

       return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        It updates the updated_at attribute with the current time and date
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        result = self.__dict__.copy()
        result['__class__'] = type(self).__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        return result 
