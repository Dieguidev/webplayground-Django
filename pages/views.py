from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page


# Create your views here.
class PageListView(ListView): 
    model = Page
    

class PageDetailView(DetailView): 
    model = Page
    
#* vistaa para crear paginas
class PageCreate(CreateView):
    model = Page
    fields = ['title', 'content', 'order']