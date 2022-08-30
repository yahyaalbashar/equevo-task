from abc import ABC, abstractmethod


class AbstractCustomStorage(ABC):
    '''
    Storage abstract class
    '''
    @abstractmethod
    def create_storage(self, path=None):
        '''
        A method that is responsible for creating storage instances to be used when having FileFields in your models.
        '''
        pass


class CustomFileSystemStorage(AbstractCustomStorage):
    '''
    Django File system storage strategy that implements AbstractCustomStorage.
    '''

    def create_storage(self, path=None):
        from django.core.files.storage import FileSystemStorage
        fs =  FileSystemStorage(location=path)
        return fs


class S3Storage(AbstractCustomStorage):
    '''
    AWS S3 storage strategy that implements AbstractCustomStorage.
    '''
    def create_storage(self, path= None):
        from storages.backends.s3boto3 import S3Boto3Storage
        custom_domain = 'equevotask.s3.me-south-1.amazonaws.com'
        fs =  S3Boto3Storage(bucket_name=path, custom_domain=custom_domain)
        return fs

