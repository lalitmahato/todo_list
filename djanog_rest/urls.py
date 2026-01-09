from django.urls import path
from djanog_rest.views import testing_rest

urlpatterns = [
    path('', testing_rest, name='testing_rest'),
]