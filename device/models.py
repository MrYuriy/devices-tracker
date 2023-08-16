from django.db import models


class DeviceSite(models.Model):
    """
    like EMAG 445 493 999
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DeviceDepartment(models.Model):
    """
    like: Kontrola Wydanie
    """
    name = models.CharField(max_length=255)
    site = models.ForeignKey(DeviceSite, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "site"], name="unique_department")
        ]

    def __str__(self):
        return self.name


class DeviceStatus(models.Model):
    """
    like: warehouse ,service ...
    """

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Devise status"
        verbose_name_plural = "Devises status"

    def __str__(self):
        return self.name


class DeviceType(models.Model):
    """
    like: barcode scaner, mobile printer ...
    """

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class DevicePort(models.Model):
    """
    ports for barcode scaner
    """

    name = models.IntegerField(unique=True)
    site = models.ForeignKey(DeviceSite, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.site}"


class DeviceIP(models.Model):
    """
    IP for printers
    """
    ip = models.GenericIPAddressField(unique=True)
    department = models.ForeignKey(DeviceDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return f"IP: {self.ip}"


class Device(models.Model):
    device_type = models.ForeignKey(DeviceType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    device_serial_number = models.CharField(max_length=255, unique=True)
    device_status = models.ForeignKey(DeviceStatus, on_delete=models.CASCADE)
    device_ip = models.ForeignKey(DeviceIP, blank=True, null=True, related_name="devices", on_delete=models.SET_NULL)
    device_ports = models.ManyToManyField(
        DevicePort,
        related_name="devices",
        blank=True,
    )
    department = models.ForeignKey(DeviceDepartment, on_delete=models.CASCADE, related_name="devices")
    device_model = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.device_type} {self.name}: {self.device_serial_number}"
