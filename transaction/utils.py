from transaction.models import Transaction
from pprint import pprint
from collections.abc import MutableMapping
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from datetime import date

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


def write_report_gs(data, sheet_name):
    body = {"values": data}

    num_rows = len(data)
    num_cols = len(data[0])

    # Генеруємо діапазон у форматі 'Sheet1!A1:{last_column}{last_row}'
    last_column = chr(ord("A") + num_cols - 1)
    last_row = num_rows

    range_ = f"{sheet_name}!A1:{last_column}{last_row}"

    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=f"{sheet_name}",
    ).execute()

    result = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=range_,
            valueInputOption="RAW",
            includeValuesInResponse=True,
            body=body,
        )
        .execute()
    )


def write_dev_change_to_spreadsheet(
    row_to_write, row_index, previous_row, line_of_position_column, spread_sheet_name
):
    """function for writing to google sheet"""

    for list_index, column_name in enumerate(line_of_position_column):
        if column_name == "Notatka":
            row_to_write[list_index] = (
                previous_row[list_index] + "\n" + row_to_write[list_index]
            )

    num_columns = len(row_to_write)
    end_column_letter = chr(
        64 + num_columns
    )  # Перетворюємо число в літеру стовпця (A=1, B=2, ...)
    update_range = f"{spread_sheet_name}!A{row_index}:{end_column_letter}{row_index}"

    value_input_option = "RAW"
    values = [row_to_write]

    # Виклик API для оновлення даних
    request = (
        service.spreadsheets()
        .values()
        .update(
            spreadsheetId=spreadsheet_id,
            range=update_range,
            valueInputOption=value_input_option,
            body={"values": values},
        )
    )
    response = request.execute()


def generate_line_to_write(device, line_of_position_column, notes):
    result_line = []
    # a = "PORT 445"
    # print("!!!!!!!")
    # print((device.device_ports.filter(site__name__icontains=a.split()[1]))[0].name)
    for field in line_of_position_column:
        if field == "S/N":
            result_line.append(device.device_serial_number)
        elif "PORT" in field.split():
            port = device.device_ports.filter(site__name__icontains=field.split()[1])
            result_line.append(
                port.values("name")[0]["name"] if port.values("name") else ""
            )
        elif field == "SITE":
            result_line.append(device.department.site.name)
        elif field == "Nazwa":
            result_line.append(device.name)
        elif field == "MODEL":
            result_line.append(device.device_model)
        elif field == "STATUS":
            result_line.append(device.device_status.name)
        elif field == "Notatka":
            result_line.append(notes)
        elif field == "IP":
            result_line.append(device.device_ip.ip)
        else:
            result_line.append("")

    return result_line


def read_from_spreadsheet(device, notes):
    """function for reading from google sheet and searching for a value"""
    # Retrieve data from the Google Sheets
    response = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id, range=device.device_type.name
        )  # Change "Sheet1" to your actual sheet name
        .execute()
    )

    device_coordinate = None
    previous_row = None

    values = response.get("values", [])
    line_of_position_column = values[2]
    # Search for the value in the specified column
    for row_index, row_values in enumerate(values):
        if device.name in row_values:
            device_coordinate = row_index + 1
            previous_row = row_values
            if len(line_of_position_column) > len(previous_row):
                previous_row.extend(
                    [
                        ""
                        for i in range(len(line_of_position_column) - len(previous_row))
                    ]
                )
            break
    row_to_write = generate_line_to_write(
        line_of_position_column=line_of_position_column, device=device, notes=notes
    )
    write_dev_change_to_spreadsheet(
        row_to_write=row_to_write,
        row_index=device_coordinate,
        previous_row=previous_row,
        line_of_position_column=line_of_position_column,
        spread_sheet_name=device.device_type.name,
    )


def create_transaction(user, device, changed_fields: dict) -> None:
    # {'department': {'old_value': 'KONTROLA', 'new_value': 'PREPARACJA'}}

    notes = f"{date.today()} User: {user.username} "

    for field, value_dikt in changed_fields.items():
        if field == "device_type":
            notes += (
                f"changed device typ {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "name":
            notes += (
                f"changed device name {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "device_serial_number":
            notes += (
                f"changed device serial number {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} and create new device "
            )
        if field == "device_status":
            notes += (
                f"changed device status {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "device_ip":
            notes += (
                f"changed device ip {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "device_ports":
            notes += (
                f"changed device ports {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "department":
            notes += (
                f"changed device status {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )
        if field == "device_model":
            notes += (
                f"changed device model {value_dikt['old_value']} "
                f"to {value_dikt['new_value']} "
            )

    transaction = Transaction(user=user, device=device, notes=notes)
    transaction.save()
    read_from_spreadsheet(device=device, notes=notes)
