from django.db import models
from django.db.models import ForeignKey


class Thermostats(models.Model):
    type = models.CharField(max_length=120)
    icon = models.ImageField(upload_to="images/", null=True, blank=True)
    def __str__(self):
        return self.type

class Thermostat(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    name = models.CharField(max_length=120)
    price = models.FloatField(max_length=1000)
    manufacturer = models.CharField(max_length=120)
    country_manufacturer = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    available = models.BooleanField(default=True)
    description = models.CharField(max_length=12000)
    description_block = models.CharField(max_length=12000)
    charge_block = models.CharField(max_length=120)
    control_range = models.CharField(max_length=120)
    max_load = models.CharField(max_length=120)
    type_connection = models.CharField(max_length=120)
    type_device = models.CharField(max_length=120)
    thermostats = models.ForeignKey(Thermostats, related_name="thermostat", on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ThermostatImages(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    thermostat_image = models.ForeignKey(Thermostat, related_name="thermostat", on_delete=models.CASCADE)
    def __str__(self):
        return self.thermostat.name

class HeatedMats(models.Model):
    name = models.CharField(max_length=120)
    count = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    fullname = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class Blog(models.Model):
    article = models.CharField(max_length=120)
    text = models.TextField(max_length=1000)
    text_two = models.TextField(max_length=1000)
    def __str__(self):
        return self.article
class ImageBlog(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    status = models.CharField(max_length=120)
    blog = ForeignKey(Blog, related_name="blod", on_delete=models.CASCADE)
    def __str__(self):
        return self.image.name

class Part(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    title = models.CharField(max_length=120)
    text = models.TextField()
    blog = ForeignKey(Blog, related_name="part", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class WarmFloor(models.Model):
    logo = models.ImageField(upload_to="images/", null=True, blank=True)
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.CharField(max_length=1000)
    model = models.CharField(max_length=120)
    history = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class ModelRange(models.Model):
    name = models.CharField(max_length=120)
    length = models.IntegerField()
    power = models.CharField(max_length=120)
    price = models.FloatField(max_length=1000)
    model_range = ForeignKey(WarmFloor, related_name="warm_floor", on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class MethodPay(models.Model):
    icon = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.description
class Produce(models.Model):
    icon = models.ImageField(upload_to="images/", null=True, blank=True)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    date_work = models.DateField()
    sphere = models.CharField(max_length=120)
    def __str__(self):
        return self.name
class HistoryApplication(models.Model):
    status = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    operator = models.CharField(max_length=120)
    def __str__(self):
        return self.operator
class Applications(models.Model):
    status = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    part = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    application = models.ForeignKey(HistoryApplication, related_name="application", on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class History(models.Model):
    operator = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    data = models.DateField()
    def __str__(self):
        return self.operator

class HotCable(models.Model):
    name = models.CharField(max_length=120)
    count = models.IntegerField(default=0)
    price = models.FloatField()
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    status = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class LetsCooperate(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    email = models.EmailField()
    status = models.CharField(max_length=120)
    operator = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    def __str__(self):
        return self.name

class CalculatePrice(models.Model):
    subject = models.CharField(max_length=120)
    procedure = models.CharField(max_length=120)
    stage = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    produce = models.CharField(max_length=120)
    type_across = models.CharField(max_length=120)
    install = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    history = models.CharField(max_length=120)
    def __str__(self):
        return self.subject
