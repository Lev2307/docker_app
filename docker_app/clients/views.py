from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import FLname
from .forms import FLnameForm

# Create your views here.
class View(ListView):
    model = FLname
    template_name = 'index.html'
    context_object_name = 'clients'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FLnameForm()         
        return context

class CreateFL(CreateView):
    model = FLname
    form_class = FLnameForm
    success_url = reverse_lazy("index")