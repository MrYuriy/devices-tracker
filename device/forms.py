from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from device.models import (
    DeviceDepartment,
    DeviceIP,
    DevicePort
)


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