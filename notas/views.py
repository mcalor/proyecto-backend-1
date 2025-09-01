from django.shortcuts import render 
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView,DeleteView, DetailView
# Create your views here.
from .models import Nota
from .forms import NotaForm
# asdasd

class NotaListView(ListView):
    model = Nota
    template_name = 'notas/lista.html'
    context_object_name = 'notas'

class NotaDetailView(DetailView):
    model = Nota
    template_name = 'notas/detalle.html'
    context_object_name = 'nota'
    pk_url_kwarg = 'id'

class NotaCreateView(CreateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/form.html'
    success_url = reverse_lazy('lista-notas')

    def form_valid(self, form):
        messages.success(self.request, "Nota creada correctamente.")
        return super().form_valid(form)
    
class NotaUpdateView(UpdateView):
    model = Nota
    form_class = NotaForm
    template_name = 'notas/form.html'
    success_url = reverse_lazy('lista-notas')
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        messages.success(self.request, "Nota actualizada correctamente.")
        return super().form_valid(form)
    
class NotaDeleteView(DeleteView):
    model = Nota
    template_name = 'notas/confirm_delete.html'
    success_url = reverse_lazy('lista-notas')
    pk_url_kwarg = 'id'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Nota eliminada.")
        return super().delete(request, *args, **kwargs)