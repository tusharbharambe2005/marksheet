from django.urls import path
from .views import search_marksheet   # Import your view

urlpatterns = [
    path('Student/', search_marksheet, name='student-list'),
    # path('marksheet/', marksheet, name='marksheet'),
]
