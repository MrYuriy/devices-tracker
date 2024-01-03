from telegram import Bot
from django.conf import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

def set_webhook():
    webhook_url = f"{settings.BASE_URL}/telegram-webhook/"
    bot.setWebhook(webhook_url)