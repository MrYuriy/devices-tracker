from django.urls import path
from .views import not_sleep

urlpatterns = [
    path("not-sleep/", not_sleep, name=""),
]

app_name = "telegram_bot"