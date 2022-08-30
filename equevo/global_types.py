from django.db import models


class DepartmentType(models.TextChoices):
    '''
    A class used as departments choices.
    '''
    IT = (1,'IT')
    HR = (2, 'HR')
    FINANCE = (3, 'Finance')


class FileTypes:
    '''
    A class used as file types list.
    '''
    EXTENSIONS_LIST = ['.pdf', '.docx']