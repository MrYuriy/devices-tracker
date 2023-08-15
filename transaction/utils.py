from transaction.models import Transaction


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
