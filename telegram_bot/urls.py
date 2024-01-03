from django.urls import path
from .views import not_sleep, TelegramWebhookView
from .telegram_bot import set_webhook

urlpatterns = [
    path("not-sleep/", not_sleep, name=""),
    path("telegram-webhook/", TelegramWebhookView.as_view(), name="telegram_webhook"),
]
set_webhook()

app_name = "telegram_bot"
