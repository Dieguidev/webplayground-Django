from django.urls import path
from .views import *

profiles_patterns = ([
    path('', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
    ], "profiles")

























