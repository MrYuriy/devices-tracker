from django.contrib import admin
from .models import (
    DeviceSite,
    DeviceDepartment,
    DeviceStatus,
    DeviceType,
    DevicePort,
    DeviceIP,
    Device,
)
from django import forms


class MyDeviceAdminForm(forms.ModelForm):
    """
    custom form for checked reserved ports
    """

    def clean_device_ports(self):
        cleaned_ports = [port.name for port in self.cleaned_data.get("device_ports")]
        existing_device = (
            Device.objects.prefetch_related("device_ports")
            .all()
            .exclude(
                device_serial_number__icontains=self.cleaned_data.get(
                    "device_serial_number"
                )
            )
        )

        port_reserved_list = []

        for device in existing_device:
            port_reserved_list += [
                port.name
                for port in device.device_ports.all()
                if port.name in cleaned_ports
            ]
        if port_reserved_list:
            raise forms.ValidationError(
                f"Ports: {list(set(port_reserved_list))} already use"
            )

        return self.cleaned_data.get("device_ports")


class PortAdmin(admin.ModelAdmin):
    list_display = ("name", "site")
    search_fields = ("port",)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "get_ports", "device_ip")
    form = MyDeviceAdminForm

    def get_ports(self, obj):
        return ", ".join([str(port.name) for port in obj.device_ports.all()])

    get_ports.short_description = "Ports"
    filter_horizontal = ("device_ports",)


admin.site.register(Device, DeviceAdmin)
admin.site.register(DevicePort, PortAdmin)
admin.site.register(DeviceStatus)
admin.site.register(DeviceType)
admin.site.register(DeviceSite)
admin.site.register(DeviceDepartment)
admin.site.register(DeviceIP)
