from django.urls import path
from tasks.views import index, error

urlpatterns = [
    path('', index, name='main-page'),
   path('error/', error, name="error-page")
]