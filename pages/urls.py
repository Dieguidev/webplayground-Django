from django.urls import path
from .views import *

from . import views
urlpatterns = [
    path('', PageListView.as_view(), name='pages'),
    path('<int:page_id>/<slug:page_slug>/', views.page, name='page'),
]