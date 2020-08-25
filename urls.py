from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:year>', views.year_archive)
]