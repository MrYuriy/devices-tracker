from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from device.forms import DeviceDepartmentForm, DeviceIPForm, DevicePortForm

from .models import (Device, DeviceDepartment, DeviceIP, DevicePort,
                     DeviceSite, DeviceStatus, DeviceType)


# Device Site
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


# Device Department

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


# Device Status
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


# Device Type

class DeviceTypeListView(generic.ListView):
    model = DeviceType
    success_url = reverse_lazy("device:device-type-list")
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


# Device
class DeviceListView(generic.ListView):
    model = Device
    template_name = "device/device_list.html"
    context_object_name = "device_list"


class DeviceCreateView(generic.CreateView):
    model = Device
    fields = "__all__"
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_form.html"


class DeviceUpdateView(generic.UpdateView):
    model = Device
    fields = "__all__"
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_form.html"


class DeviceDeleteView(generic.DeleteView):
    model = Device
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_confirm_delete.html"


# Device Port
class DevicePortListView(generic.ListView):
    model = DevicePort
    template_name = "device/device_port_list.html"
    context_object_name = "device_port_list"


class DevicePortCreateView(generic.CreateView):
    model = DevicePort
    form_class = DevicePortForm
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_form.html"


class DevicePortUpdateView(generic.UpdateView):
    model = DevicePort
    form_class = DevicePortForm
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_form.html"


class DevicePortDeleteView(generic.DeleteView):
    model = DevicePort
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_confirm_delete.html"


# Device IP

class DeviceIPListView(generic.ListView):
    model = DeviceIP
    template_name = "device/device_ip_list.html"
    context_object_name = "device_ip_list"


class DeviceIPCreateView(generic.CreateView):
    model = DeviceIP
    form_class = DeviceIPForm
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_form.html"


class DeviceIPUpdateView(generic.UpdateView):
    model = DeviceIP
    form_class = DeviceIPForm
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_form.html"


class DeviceIPDeleteView(generic.DeleteView):
    model = DeviceIP
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_confirm_delete.html"
