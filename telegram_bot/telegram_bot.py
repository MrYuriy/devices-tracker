from telebot import TeleBot
from django.conf import settings
from transaction.utils import read_all_sheets
import pprint

bot = TeleBot(settings.TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def process_message(message_data):
    #rint(message_data)
    chat_id = message_data["message"]["chat"]["id"]
    text = message_data["message"]["text"]

    if text == "/help":
        bot.send_message(chat_id, "Witam, jestem botem, który podaje wszelkie informacje o urządzeniach, wystarczy, że wpiszesz część nazwy urządzenia lub numer seryjny ")
    else:
        sheet_data = read_all_sheets()
        info = filter_data_by_info(target_text=text, sheet_data=sheet_data)
        if len(info) > 4000:
            info = "wynik jest za długi, użyj bardziej szczegółowego filtra"
        bot.send_message(chat_id, f"{info}")

def filter_data_by_info(target_text, sheet_data):
    device_info = ""
    for sheet in sheet_data:
        for row_list in sheet:
            row = " ".join([cel for cel in row_list if cel!=""])
            if target_text.lower() in row.lower():
                device_info = device_info + "\n\n" + row.replace("\n", " ")
    if device_info == "":
        device_info = "Brak informacji"
    return device_info       