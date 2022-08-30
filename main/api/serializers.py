from rest_framework import serializers
from main.models import Candidate, Document
from main.validators import validate_file_extension

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class CandidateSerializer(serializers.ModelSerializer):
    resume = serializers.FileField(validators = [validate_file_extension])
    class Meta:
        model = Candidate
        fields = ['resume', 'full_name', 'date_of_birth', 'years_of_experience', 'department']

    def create(self, validated_data):
        resume_data = validated_data.pop('resume')
        resume = Document.objects.create(file=resume_data)
        validated_data["resume_id"] = resume.id
        instance = Candidate.objects.create(**validated_data)
        return instance


class AdminCandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
