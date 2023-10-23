from django.urls import path

from .views import (
    DeviceCreateView,
    DeviceDeleteView,
    DeviceDepartmentCreateView,
    DeviceDepartmentDeleteView,
    DeviceDepartmentListView,
    DeviceDepartmentUpdateView,
    DeviceDetailView,
    DeviceIPCreateView,
    DeviceIPDeleteView,
    DeviceIPListView,
    DeviceIPUpdateView,
    DeviceListView,
    DevicePortCreateView,
    DevicePortDeleteView,
    DevicePortListView,
    DevicePortUpdateView,
    DeviceSiteCreateView,
    DeviceSiteDeleteView,
    DeviceSiteListView,
    DeviceSiteUpdateView,
    DeviceStatusCreateView,
    DeviceStatusDeleteView,
    DeviceStatusListView,
    DeviceStatusUpdateView,
    DeviceTypeCreateView,
    DeviceTypeDeleteView,
    DeviceTypeListView,
    DeviceTypeUpdateView,
    DeviceUpdateView,
    HomeView,
    ReportsView,
    UpdateInventoryView,
)

urlpatterns = [
    path("device-sites/", DeviceSiteListView.as_view(), name="device-site-list"),
    path(
        "device-sites/create", DeviceSiteCreateView.as_view(), name="device-site-create"
    ),
    path(
        "device-sites/<int:pk>/update/",
        DeviceSiteUpdateView.as_view(),
        name="device-site-update",
    ),
    path(
        "device-sites/<int:pk>/delete/",
        DeviceSiteDeleteView.as_view(),
        name="device-site-delete",
    ),
    path(
        "device-departments/",
        DeviceDepartmentListView.as_view(),
        name="device-department-list",
    ),
    path(
        "device-departments/create",
        DeviceDepartmentCreateView.as_view(),
        name="device-department-create",
    ),
    path(
        "device-departments/<int:pk>/update/",
        DeviceDepartmentUpdateView.as_view(),
        name="device-department-update",
    ),
    path(
        "device-departments/<int:pk>/delete/",
        DeviceDepartmentDeleteView.as_view(),
        name="device-department-delete",
    ),
    path("device-statuses/", DeviceStatusListView.as_view(), name="device-status-list"),
    path(
        "device-statuses/create",
        DeviceStatusCreateView.as_view(),
        name="device-status-create",
    ),
    path(
        "device-statuses/<int:pk>/update/",
        DeviceStatusUpdateView.as_view(),
        name="device-status-update",
    ),
    path(
        "device-statuses/<int:pk>/delete/",
        DeviceStatusDeleteView.as_view(),
        name="device-status-delete",
    ),
    path("device-types/", DeviceTypeListView.as_view(), name="device-type-list"),
    path(
        "device-types/create", DeviceTypeCreateView.as_view(), name="device-type-create"
    ),
    path(
        "device-types/<int:pk>/update/",
        DeviceTypeUpdateView.as_view(),
        name="device-type-update",
    ),
    path(
        "device-types/<int:pk>/delete/",
        DeviceTypeDeleteView.as_view(),
        name="device-type-delete",
    ),
    path("device-ports/", DevicePortListView.as_view(), name="device-port-list"),
    path(
        "device-ports/create", DevicePortCreateView.as_view(), name="device-port-create"
    ),
    path(
        "device-ports/<int:pk>/update/",
        DevicePortUpdateView.as_view(),
        name="device-port-update",
    ),
    path(
        "device-ports/<int:pk>/delete/",
        DevicePortDeleteView.as_view(),
        name="device-port-delete",
    ),
    path("device-ips/", DeviceIPListView.as_view(), name="device-ip-list"),
    path("device-ips/create", DeviceIPCreateView.as_view(), name="device-ip-create"),
    path(
        "device-ips/<int:pk>/update/",
        DeviceIPUpdateView.as_view(),
        name="device-ip-update",
    ),
    path(
        "device-ips/<int:pk>/delete/",
        DeviceIPDeleteView.as_view(),
        name="device-ip-delete",
    ),
    path("devices/", DeviceListView.as_view(), name="device-list"),
    path("devices/create", DeviceCreateView.as_view(), name="device-create"),
    path("devices/<int:pk>/detail", DeviceDetailView.as_view(), name="device-detail"),
    path("devices/<int:pk>/update/", DeviceUpdateView.as_view(), name="device-update"),
    path("devices/<int:pk>/delete/", DeviceDeleteView.as_view(), name="device-delete"),
    path("", HomeView.as_view(), name="home"),
    path("report", ReportsView.as_view(), name="reports"),
    path(
        "devices/inventarisation/",
        UpdateInventoryView.as_view(),
        name="inventarisation",
    ),
]

app_name = "device"
