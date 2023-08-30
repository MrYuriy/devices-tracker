import openpyxl
from device.models import (
    DevicePort,
    DeviceSite,
    Device,
    DeviceType,
    DeviceStatus,
    DeviceDepartment,
    DeviceIP,
)

from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist


def department_site_split(site_department: str):
    if "(" in site_department:
        site = site_department.split()[0]
        department = site_department.split()[1]
        department = department.replace("(", "")
        department = department.replace(")", "")
        department = department.replace(" ", "")
    else:
        department = ""
        site = site_department
    site = site.replace(" ", "")
    return {"department": str(department).upper(), "site": str(site).upper()}


def get_device_row(sheet):
    line_device_fields = [cell.value for cell in sheet[1]]
    devices = []
    for row in sheet.iter_rows(min_row=2):
        device_dictionary = {}
        for index, cell in enumerate(line_device_fields):
            device_dictionary[cell] = row[index].value
        devices.append(device_dictionary)
    return devices


def create_device(sheet, dev_type):
    devices = get_device_row(sheet)

    for device in devices:
        with transaction.atomic():
            department = department_site_split(str(device["SITE"]))

            device_type, _ = DeviceType.objects.get_or_create(name=dev_type)
            device_status, _ = DeviceStatus.objects.get_or_create(name="WORK")
            site, _ = DeviceSite.objects.get_or_create(
                name=str(department["site"]).upper()
            )
            department_obj, _ = DeviceDepartment.objects.get_or_create(
                name=str(department["department"]).upper(), site=site
            )

            dev = Device(
                device_type=device_type,
                name=device["Nazwa"],
                device_serial_number=device["S/N"],
                device_status=device_status,
                department=department_obj,
                device_model=device["MODEL"],
            )
            dev.save()

            ports_to_check = ["PORT EMAG", "PORT 445", "PORT 999"]
            for port_key in ports_to_check:
                if port_key in device:
                    if device[port_key] is not None:
                        try:
                            port_site = (
                                str(port_key.split()[1]).upper().replace(" ", "")
                            )
                            site, _ = DeviceSite.objects.get_or_create(name=port_site)
                            port, _ = DevicePort.objects.get_or_create(
                                name=device[port_key], site=site
                            )
                            dev.device_ports.add(port)
                        except ObjectDoesNotExist:
                            pass
            if "IP" in device:
                try:
                    device_ip, _ = DeviceIP.objects.get_or_create(
                        ip=device["IP"], department=department_obj
                    )
                    dev.device_ip = device_ip
                except ObjectDoesNotExist:
                    pass
            dev.save()
            print(dev)


# create_ports()


def main():
    workbook = openpyxl.load_workbook("device_list.xlsx")
    devices_type = ["SCANER", "PRINTER"]
    for device_type in devices_type:
        sheet = workbook[device_type]
        create_device(sheet, device_type)


main()
