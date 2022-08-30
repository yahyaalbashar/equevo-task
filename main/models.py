from equevo.global_types import DepartmentType

from main.validators import validate_file_extension
from main.storage import STORAGE

from django.db import models


class Candidate(models.Model):
    '''
    A Django model to represent Candidates
    '''
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    years_of_experience = models.PositiveIntegerField()
    department = models.CharField(max_length= 255, choices=DepartmentType.choices)
    resume = models.OneToOneField('Document', on_delete=models.CASCADE, related_name="candidate")

    def __str__(self):
        return self.full_name


class Document(models.Model):
    '''
    A Django model to represent document
    '''
    file = models.FileField(upload_to="documents/", validators=[validate_file_extension], storage= STORAGE)