from django.urls import path

from .views import (
    newjob,
)

app_name='quotes'
urlpatterns = [
    path("kruegerprint/", newjob, name='krueger-print'),
]