from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from telegram import Update

from .telegram_bot import bot  # Import the bot object


def not_sleep(request):
    return HttpResponse(status=200)


class TelegramWebhookView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        update = Update.de_json(json.loads(request.body.decode('utf-8')), bot)
        process_message(update.message)
        return JsonResponse({'status': 'ok'})

def process_message(message):
    chat_id = message.chat_id
    text = message.text

    if text.startswith('/help'):
        send_help_message(chat_id)
    else:
        # Echo the received message
        send_message(chat_id, f"You said: {text}")

def send_help_message(chat_id):
    help_text = (
        "Welcome to the Echo Bot!\n"
        "Commands available:\n"
        "/help - Show this help message\n"
        "Any other text - Echo back your message"
    )
    send_message(chat_id, help_text)

def send_message(chat_id, text):
    bot.send_message(chat_id, text)