from django.shortcuts import render
from .models import Emp
from django.views.generic import TemplateView,CreateView,UpdateView,ListView,DeleteView
class Index(CreateView):
    model = Emp
    template_name = "index.html"
    fields = ["idno","name","salary"]
    success_url = "/home/"


class Update(UpdateView):
    model = Emp
    template_name = "Update.html"
    fields = ["idno", "name", "salary"]
    success_url = "/home/"


class Delete(DeleteView):
    model = Emp
    template_name = "Delete.html"
    fields = ["idno", "name", "salary"]
    success_url = "/home/"
