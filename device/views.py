from django.shortcuts import render
from django.views import generic

from .models import Site

class SiteListView(generic.ListView):
    model = Site
    