from models.engine.file_storage import FileStorage
storage = FileStorage("file.json")
storage.reload()

# we then make the instance storage a global variable
#This will allow the access of storage class by other modules in the application
#by importing the app_storage
app_storage = storage
# with this set up we can use app_storage to handle file related operations throught
# my application and all objects created in my application will be stored and loaded from file.json
