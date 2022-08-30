from main.models import Candidate, Document
from .serializers import (
                            CandidateSerializer, 
                            AdminCandidateSerializer,
                            DocumentSerializer
                         )
from rest_framework.generics import (
                                        CreateAPIView, 
                                        ListAPIView, 
                                        RetrieveAPIView
                                    )
from django.core.exceptions import PermissionDenied

class RegisterCandidateAPIView(CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_queryset(self):
        return super().get_queryset()


class ListCandidatesAPIView(ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = AdminCandidateSerializer

    def get_queryset(self):
        if "HTTP_X_ADMIN" in self.request.META and self.request.META["HTTP_X_ADMIN"] == "1":
            return super().get_queryset()
        else:
            raise PermissionDenied()


class RetrieveCandidateResume(RetrieveAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    lookup_field = "candidate"


    def get_queryset(self):
        if "HTTP_X_ADMIN" in self.request.META and self.request.META["HTTP_X_ADMIN"] == "1":
            return super().get_queryset()
        else:
            raise PermissionDenied()