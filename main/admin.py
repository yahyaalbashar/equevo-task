from django.contrib import admin
from .models import Candidate, Document


@admin.register(Candidate)
class AdminCandidate(admin.ModelAdmin):
    pass


@admin.register(Document)
class AdminDocument(admin.ModelAdmin):
    pass