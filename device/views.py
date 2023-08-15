from django.shortcuts import render
from django.views import generic

from .models import DeviceSite, Device

class SiteListView(generic.ListView):
    model = DeviceSite
    template_name = "device/device_site_list.html"
    context_object_name = "device_site_list"


class SiteCreateView(generic.CreateView):
    model = DeviceSite
    fields = "__all__"
    success_url = "device:site-list"
    template_name = "device/device_site_form.html"


class DeviceListView(generic.ListView):
    model = Device
    template_name = "device/device_list.html"
    context_object_name = "device_list"
