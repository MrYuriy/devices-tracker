from transaction.models import Transaction
from pprint import pprint
from collections.abc import MutableMapping
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings


# open credential file
CREDENTIALS_FILE = "creds.json"
# ID Google Sheets documents
spreadsheet_id = settings.SPREADSHEET_ID

# service — API access instance
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ],
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build("sheets", "v4", http=httpAuth)


def write_to_spreadsheet():
    """function for writing to google sheet"""
    pass


def read_from_spreadsheet(search_value, column_index):
    """function for reading from google sheet and searching for a value"""
    # Retrieve data from the Google Sheets
    response = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range="SKANER")  # Change "Sheet1" to your actual sheet name
        .execute()
    )

    # Extract values from the response
    values = response.get("values", [])

    found_cells = []
    print(search_value )
    # Search for the value in the specified column
    for row_index, row_values in enumerate(values):
        if search_value in row_values:
            print(row_index, row_values.index(search_value))




def create_transaction(user, device, changed_fields: dict) -> None:
    # {'department': {'old_value': 'KONTROLA', 'new_value': 'PREPARACJA'}}

    notes = f"User: {user.username} "

    for field, value_dikt in changed_fields.items():
        if field == "device_type":
            notes += f"changed device typ {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "name":
            notes += f"changed device name {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "device_serial_number":
            notes += f"changed device serial number {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} and create new device "
        if field == "device_status":
            notes += f"changed device status {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "device_ip":
            notes += f"changed device ip {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "device_ports":
            notes += f"changed device ports {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "department":
            notes += f"changed device status {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "
        if field == "device_model":
            notes += f"changed device model {value_dikt['old_value']} " \
                     f"to {value_dikt['new_value']} "

    notes += f"in {device.name}."

    transaction = Transaction(user=user, device=device, notes=notes)
    transaction.save()
    read_from_spreadsheet(search_value=device.name, column_index=6)
