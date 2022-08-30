from equevo.global_types import FileTypes

def validate_file_extension(value):
    """
        Description: used to validate an uploaded file extension
        input: file path
        output: raises a validation error if the file type is not one of the valid extensions (PDF, DOCX)
    """
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = FileTypes.EXTENSIONS_LIST
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Please make sure that your file is either PDF or DOCX format!')