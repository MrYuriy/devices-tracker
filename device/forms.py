from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from device.models import Device, DeviceDepartment, DeviceIP, DevicePort


class DeviceDepartmentForm(forms.ModelForm):
    site = forms.CheckboxInput()

    class Meta:
        model = DeviceDepartment
        fields = "__all__"


class DevicePortForm(forms.ModelForm):
    name = forms.IntegerField()
    site = forms.CheckboxInput()

    class Meta:
        model = DevicePort
        fields = "__all__"


class DeviceIPForm(forms.ModelForm):
    department = forms.CheckboxInput()

    class Meta:
        model = DeviceIP
        fields = "__all__"


class DeviceUpdateCreateForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        available_ports = DevicePort.objects.filter(Q(devices__isnull=True) | Q(devices=self.instance))
        available_ip = DeviceIP.objects.filter(Q(devices__isnull=True) | Q(devices=self.instance))

        self.fields["device_ports"].queryset = available_ports
        self.fields["device_ip"].queryset = available_ip


class DeviceSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name or serial number"}
        )
    )