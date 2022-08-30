from django.urls import path
from .api.views import (
                            RegisterCandidateAPIView, 
                            ListCandidatesAPIView,
                            RetrieveCandidateResume
                        )

urlpatterns = [
    path('register-candidate/', RegisterCandidateAPIView.as_view(), name= "register_candidate"),
    path('list-candidates', ListCandidatesAPIView.as_view(), name = "list_candidates"),
    path('candidate-resume/<candidate>', RetrieveCandidateResume.as_view(), name = "candidate_document"),
]