from equevo.storage_methods import S3Storage #,CustomFileSystemStorage 

from django.conf import settings
from django.utils.deconstruct import deconstructible 

@deconstructible
class CustomStorage:
    '''
    A storage class that's responsible for storage. storage_method is a storage object injected as dependecy.
    '''
    def __init__(self, storage_method= None):
        self.storage_method = storage_method

    def get_storage(self,  path):
        '''
        Description: a method that returns a file storage object eg: FileStorage or S3Storage.

        arguments: path:str (string path to where files are stored)
        '''
        return self.storage_method.create_storage(path= path)


# example usage:

# S3 storage
STORAGE = CustomStorage(S3Storage()).get_storage(settings.AWS_STORAGE_BUCKET_NAME)

# FileSystemStorage, uncomment to use it, also uncomment it's import.
# STORAGE = CustomStorage(CustomFileSystemStorage()).get_storage('documents/')
