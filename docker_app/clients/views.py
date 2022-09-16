from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from .models import Firstlastname
from .forms import FirstlastnameForm
# Create your views here.
class View(ListView):
    model = Firstlastname
    template_name = 'index.html'
    context_object_name = 'clients'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FirstlastnameForm()         
        return context


class CreateFL(CreateView):
    model = Firstlastname
    form_class = FirstlastnameForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.mr_save()
        return super().form_valid(form)