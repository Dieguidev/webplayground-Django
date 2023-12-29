from django.urls import path
from .views import *

messenger_patterns = ([
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='detail'),
], 'messenger')