from django.urls import path,include 
from .views import RetrieveBooks

urlpatterns = [ 
    path('book/',RetrieveBooks.as_view())
]