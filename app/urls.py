from django.urls import path, include
from .views import get_all_files, home
urlpatterns = [
    path('', home, name='home'),
    path('all-files', get_all_files, name='all_files'),
]
