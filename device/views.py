from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from device.forms import DeviceDepartmentForm

from .models import DeviceDepartment, DeviceSite, DeviceStatus, DeviceType


#Device Site
class DeviceSiteListView(generic.ListView):
    model = DeviceSite
    template_name = "device/device_site_list.html"
    context_object_name = "device_site_list"


class DeviceSiteCreateView(generic.CreateView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_form.html"


class DeviceSiteUpdateView(generic.UpdateView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_form.html"


class DeviceSiteDeleteView(generic.DeleteView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_confirm_delete.html"

#Device Department

class DeviceDepartmentListView(generic.ListView):
    model = DeviceDepartment
    template_name = "device/device_department_list.html"
    context_object_name = "device_department_list"


class DeviceDepartmentCreateView(generic.CreateView):
    model = DeviceDepartment
    form_class = DeviceDepartmentForm
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_form.html"


class DeviceDepartmentUpdateView(generic.UpdateView):
    model = DeviceDepartment
    form_class = DeviceDepartmentForm
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_form.html"


class DeviceDepartmentDeleteView(generic.DeleteView):
    model = DeviceDepartment
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_confirm_delete.html"

#Device Status
class DeviceStatusListView(generic.ListView):
    model = DeviceStatus
    template_name = "device/device_status_list.html"
    context_object_name = "device_status_list"


class DeviceStatusCreateView(generic.CreateView):
    model = DeviceStatus
    fields = "__all__"
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_form.html"


class DeviceStatusUpdateView(generic.UpdateView):
    model = DeviceStatus
    fields = "__all__"
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_form.html"


class DeviceStatusDeleteView(generic.DeleteView):
    model = DeviceStatus
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_confirm_delete.html"

#Device Type

class DeviceTypeListView(generic.ListView):
    model = DeviceType
    template_name = "device/device_type_list.html"
    context_object_name = "device_type_list"


class DeviceTypeCreateView(generic.CreateView):
    model = DeviceType
    fields = "__all__"
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_form.html"


class DeviceTypeUpdateView(generic.UpdateView):
    model = DeviceType
    fields = "__all__"
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_form.html"


class DeviceTypeDeleteView(generic.DeleteView):
    model = DeviceType
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_confirm_delete.html"
