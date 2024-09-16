from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from device.models import DeviceSite
from user.models import User


class UserCreationForm(UserCreationForm):
    site = forms.ModelMultipleChoiceField(
        queryset=DeviceSite.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
             "email",  "site"
        )


class UserUpdateForm(forms.ModelForm):
    site = forms.ModelMultipleChoiceField(
        queryset=DeviceSite.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)  # New password field
    class Meta:
        model = User
        fields = ["username", "site", "new_password"]


class UserSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"}
        )
    )