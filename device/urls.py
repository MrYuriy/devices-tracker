from django.urls import path
from .views import (
    DeviceListView,
    DeviceCreateView,
    DeviceUpdateView,
    DeviceDeleteView,

    DeviceSiteListView,
    DeviceSiteCreateView,
    DeviceSiteUpdateView,
    DeviceSiteDeleteView,

    DeviceDepartmentListView,
    DeviceDepartmentCreateView,
    DeviceDepartmentUpdateView,
    DeviceDepartmentDeleteView,

    DeviceStatusListView,
    DeviceStatusCreateView,
    DeviceStatusUpdateView,
    DeviceStatusDeleteView,

    DeviceTypeListView,
    DeviceTypeCreateView,
    DeviceTypeUpdateView,
    DeviceTypeDeleteView,
)
urlpatterns = [
    path(
        "device-sites/",
        DeviceSiteListView.as_view(),
        name="device-site-list"
    ),

    path(
        "device-sites/create",
        DeviceSiteCreateView.as_view(),
        name="device-site-create"
    ),

    path(
        "device-sites/<int:pk>/update/",
        DeviceSiteUpdateView.as_view(),
        name="device-site-update"
    ),

    path(
        "device-sites/<int:pk>/delete/",
        DeviceSiteDeleteView.as_view(),
        name="device-site-delete"
    ),

    path(
        "device-departments/",
        DeviceDepartmentListView.as_view(),
        name="device-department-list"
    ),

    path(
        "device-departments/create",
        DeviceDepartmentCreateView.as_view(),
        name="device-department-create"
    ),

    path(
        "device-departments/<int:pk>/update/",
        DeviceDepartmentUpdateView.as_view(),
        name="device-department-update"
    ),

    path(
        "device-departments/<int:pk>/delete/",
        DeviceDepartmentDeleteView.as_view(),
        name="device-department-delete"
    ),

    path(
        "device-statuses/",
        DeviceStatusListView.as_view(),
        name="device-status-list"
    ),

    path(
        "device-statuses/create",
        DeviceStatusCreateView.as_view(),
        name="device-status-create"
    ),

    path(
        "device-statuses/<int:pk>/update/",
        DeviceStatusUpdateView.as_view(),
        name="device-status-update"
    ),

    path(
        "device-statuses/<int:pk>/delete/",
        DeviceStatusDeleteView.as_view(),
        name="device-status-delete"
    ),

    path(
        "device-types/",
        DeviceTypeListView.as_view(),
        name="device-type-list"
    ),

    path(
        "device/create",
        DeviceCreateView.as_view(),
        name="device-create"
    ),

    path(
        "device/<int:pk>/update/",
        DeviceUpdateView.as_view(),
        name="device-update"
    ),

    path(
        "device/<int:pk>/delete/",
        DeviceDeleteView.as_view(),
        name="device-delete"
    ),
    path(
        "devices/",
        DeviceListView.as_view(),
        name="device-list"

    ),
]

app_name = "device"
