from django.shortcuts import render
from django.views.generic.detail import DetailView 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Thread
from django.http import Http404



# Create your views here.

#esta vista es para que el usuario no pueda acceder a la vista de los mensajes si no esta logeado y además debido a la relacion con users filtra solo sus threads
@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"


@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
    
    #metodo para que el usuario no pueda acceder a los mensajes de otros usuarios si no esta logeado
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj