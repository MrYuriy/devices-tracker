from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .telegram_bot import bot, process_message  # Import the bot object


def not_sleep(request):
    return HttpResponse(status=200)


class TelegramWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        message_data = request.data
        #print(message_data)
        process_message(message_data)
        return JsonResponse({'status': 'ok'})

