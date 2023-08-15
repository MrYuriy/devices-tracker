from django.urls import path
from .views import (
    SiteListView,
    SiteCreateView,
    DeviceListView,
)
urlpatterns = [
    path(
        "sites/",
        SiteListView.as_view(),
        name="site-list"
    ),

    path(
        "sites/create",
        SiteCreateView.as_view(),
        name="site-create"
    ),
    path(
        "devices/",
        DeviceListView.as_view(),
        name="device-list"

    ),
]

app_name = "device"
