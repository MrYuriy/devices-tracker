from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView

from device.forms import (DeviceDepartmentForm, DeviceIPForm, DevicePortForm,
                          DeviceSearchForm, DeviceUpdateForm)
from transaction.utils import create_transaction

from .models import (Device, DeviceDepartment, DeviceIP, DevicePort,
                     DeviceSite, DeviceStatus, DeviceType)


# Device Site
class DeviceSiteListView(LoginRequiredMixin, generic.ListView):
    model = DeviceSite
    template_name = "device/device_site_list.html"
    context_object_name = "device_site_list"


class DeviceSiteCreateView(LoginRequiredMixin, generic.CreateView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_form.html"


class DeviceSiteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_form.html"


class DeviceSiteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DeviceSite
    fields = "__all__"
    success_url = reverse_lazy("device:device-site-list")
    template_name = "device/device_site_confirm_delete.html"


# Device Department

class DeviceDepartmentListView(LoginRequiredMixin, generic.ListView):
    model = DeviceDepartment
    template_name = "device/device_department_list.html"
    context_object_name = "device_department_list"


class DeviceDepartmentCreateView(LoginRequiredMixin, generic.CreateView):
    model = DeviceDepartment
    form_class = DeviceDepartmentForm
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_form.html"


class DeviceDepartmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DeviceDepartment
    form_class = DeviceDepartmentForm
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_form.html"


class DeviceDepartmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DeviceDepartment
    success_url = reverse_lazy("device:device-department-list")
    template_name = "device/device_department_confirm_delete.html"


# Device Status
class DeviceStatusListView(LoginRequiredMixin, generic.ListView):
    model = DeviceStatus
    template_name = "device/device_status_list.html"
    context_object_name = "device_status_list"


class DeviceStatusCreateView(LoginRequiredMixin, generic.CreateView):
    model = DeviceStatus
    fields = "__all__"
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_form.html"


class DeviceStatusUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DeviceStatus
    fields = "__all__"
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_form.html"


class DeviceStatusDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DeviceStatus
    success_url = reverse_lazy("device:device-status-list")
    template_name = "device/device_status_confirm_delete.html"


# Device Type

class DeviceTypeListView(LoginRequiredMixin, generic.ListView):
    model = DeviceType
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_list.html"
    context_object_name = "device_type_list"


class DeviceTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DeviceType
    fields = "__all__"
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_form.html"


class DeviceTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DeviceType
    fields = "__all__"
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_form.html"


class DeviceTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DeviceType
    success_url = reverse_lazy("device:device-type-list")
    template_name = "device/device_type_confirm_delete.html"


# Device
class DeviceListView(LoginRequiredMixin, generic.ListView):
    model = Device
    template_name = "device/device_list.html"
    context_object_name = "device_list"
    paginate_by = 20

    def get_queryset(self):

        queryset = super().get_queryset()
        
        form = DeviceSearchForm(self.request.GET)
        if form.is_valid():
            queryset = queryset.filter(Q(name__icontains=form.cleaned_data["name"])|Q(device_serial_number__icontains=form.cleaned_data["name"]))

        status_id = self.request.GET.get("status")
        if status_id:
            status = get_object_or_404(DeviceStatus, pk=status_id)
            queryset = queryset.filter(device_status=status)

        device_type_id = self.request.GET.get("device_type")
        if device_type_id:
            device_type = get_object_or_404(DeviceType, pk=device_type_id)
            queryset = queryset.filter(device_type=device_type)

        department_id = self.request.GET.get("department")
        if department_id:
            department = get_object_or_404(DeviceDepartment, pk=department_id)
            queryset = queryset.filter(department=department)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['device_status_list'] = DeviceStatus.objects.all()
        context['device_type_list'] = DeviceType.objects.all()
        context['department_list'] = DeviceDepartment.objects.all()
        
        name = self.request.GET.get("name", "")
        device_serial_number = self.request.GET.get("name", "")
        context["search_form"] = DeviceSearchForm(
            initial={
                "name": name,
                "device_serial_number": device_serial_number
            }
        )

        return context


class DeviceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Device
    fields = "__all__"
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_form.html"


class DeviceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Device
    form_class = DeviceUpdateForm
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_form.html"

    def form_valid(self, form):
        original_device = self.get_object()
        new_device = form.save(commit=False)  # Don't save yet

        changes = {}  # Dictionary to store changes

        for field in new_device._meta.fields:  # Loop through all fields of the model
            field_name = field.name
            old_value = getattr(original_device, field_name)
            new_value = getattr(new_device, field_name)

            if old_value != new_value:
                changes[field_name] = {
                    'old_value': old_value,
                    'new_value': new_value
                }

        if original_device.device_serial_number != new_device.device_serial_number:
            with transaction.atomic():
                original_device.device_ports.clear()
                original_device.device_status = get_object_or_404(DeviceStatus, name="REPLACED")
                new_device.pk = None
                new_device.save()
        if changes:
            create_transaction(
                user=self.request.user,
                device=original_device,
                changed_fields=changes
            )

        original_device.save()
        return super().form_valid(form)


class DeviceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Device
    success_url = reverse_lazy("device:device-list")
    template_name = "device/device_confirm_delete.html"


# Device Port
class DevicePortListView(LoginRequiredMixin, generic.ListView):
    model = DevicePort
    template_name = "device/device_port_list.html"
    context_object_name = "device_port_list"


class DevicePortCreateView(LoginRequiredMixin, generic.CreateView):
    model = DevicePort
    form_class = DevicePortForm
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_form.html"


class DevicePortUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DevicePort
    form_class = DevicePortForm
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_form.html"


class DevicePortDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DevicePort
    success_url = reverse_lazy("device:device-port-list")
    template_name = "device/device_port_confirm_delete.html"


# Device IP

class DeviceIPListView(LoginRequiredMixin, generic.ListView):
    model = DeviceIP
    template_name = "device/device_ip_list.html"
    context_object_name = "device_ip_list"


class DeviceIPCreateView(LoginRequiredMixin, generic.CreateView):
    model = DeviceIP
    form_class = DeviceIPForm
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_form.html"


class DeviceIPUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DeviceIP
    form_class = DeviceIPForm
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_form.html"


class DeviceIPDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DeviceIP
    success_url = reverse_lazy("device:device-ip-list")
    template_name = "device/device_ip_confirm_delete.html"


class HomeView(TemplateView):
    template_name = "device/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['device_type_list'] = DeviceType.objects.all()
        return context
