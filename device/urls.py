from django.urls import path
from .views import (
    SiteListView
)
urlpatterns = [
    path(
        "sites/",
        SiteListView.as_view(),
        name="site-list"
    )
]

app_name = "device"
