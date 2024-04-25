from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.JobListCreateView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', views.JobDetailView.as_view(), name='job-detail'),
    path('applicants/', views.ApplicantListCreateView.as_view(), name='applicant-list-create'),
    path('applicants/<int:pk>/', views.ApplicantDetailView.as_view(), name='applicant-detail'),
    path('applications/', views.ApplicationListCreateView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('users/', views.CreateUserView.as_view(), name='user-create'),
]
