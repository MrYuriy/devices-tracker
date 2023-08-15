from django.urls import path
from .views import (
    SiteListView,
    SiteCreateView,
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
    )

]

app_name = "device"
