from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from . import models

class FindPassword(generic.CreateView):
    fields = ["old_password", "new_password", "confirm_new_password"]
    model = models.Account
    template_name = "find_password/rest.html"
    success_url = reverse_lazy("success")
    

class Success(generic.TemplateView):
    template_name = "find_password/success.html"
    
    