from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from device.models import (
    DeviceDepartment
)




class DeviceDepartmentForm(forms.ModelForm):
    site = forms.CheckboxInput()

    class Meta:
        model = DeviceDepartment
        fields = "__all__"