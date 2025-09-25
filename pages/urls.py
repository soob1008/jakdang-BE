from django.urls import path
from .views import PageDetailBySlugView

urlpatterns = [
    path('page/<slug:slug>', PageDetailBySlugView.as_view(), name='page-detail-slug')
]