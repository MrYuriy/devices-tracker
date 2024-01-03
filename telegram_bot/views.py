from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json


def not_sleep(request):
    return HttpResponse(status=200)


class TelegramWebhookView(View):
    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        # Implement your Telegram bot logic here
        # Handle incoming messages, process commands, etc.
        return JsonResponse({"status": "ok"})
