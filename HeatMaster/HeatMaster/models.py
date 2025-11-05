import datetime

from django.db import models
from django.db.models import ForeignKey
from django.utils import timezone


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
    # Stock available for purchase (integer). When 0, item considered out of stock.
    available = models.IntegerField(default=0)
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
    article = models.CharField(max_length=200)
    text = models.TextField(max_length=10000)
    text_two = models.TextField(max_length=10000)
    start= models.TextField(max_length=10000,default="")
    final = models.TextField(max_length=10000, default='')
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.article
class ImageBlog(models.Model):
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    status = models.CharField(max_length=120)
    blog = ForeignKey(Blog, related_name="blod", on_delete=models.CASCADE)
    def __str__(self):
        return self.image.name
class CommentBlog(models.Model):
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=320)
    username = models.CharField(max_length=320)
    rating = models.FloatField(default=0)
    blog = ForeignKey(Blog, related_name="comment", on_delete=models.CASCADE)
    def __str__(self):
        return self.author

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
    date_work = models.CharField(max_length=10)
    sphere = models.CharField(max_length=120)
    def __str__(self):
        return self.name
def get_default_application():
    return Applications.objects.first()
class Applications(models.Model):
    status = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    part = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    def __str__(self):
        return self.description
class HistoryApplication(models.Model):
    status = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    operator = models.CharField(max_length=120)
    application = models.ForeignKey(Applications, related_name="application", on_delete=models.CASCADE, default=get_default_application)
    def __str__(self):
        return self.operator
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


# --- E-commerce models ---
class Cart(models.Model):
    user = models.ForeignKey('auth.User', related_name='carts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart #{self.pk} for {self.user.username}"

    @property
    def total_price(self):
        items = getattr(self, 'items', None)
        if items is None:
            return 0
        return sum(item.subtotal for item in items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    thermostat = models.ForeignKey(Thermostat, related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'thermostat')

    def __str__(self):
        return f"{self.thermostat.name} x{self.quantity}"

    @property
    def subtotal(self):
        return float(self.thermostat.price) * int(self.quantity)


class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_PAID = 'paid'
    STATUS_SHIPPED = 'shipped'
    STATUS_COMPLETED = 'completed'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый'),
        (STATUS_PAID, 'Оплачен'),
        (STATUS_SHIPPED, 'Отправлен'),
        (STATUS_COMPLETED, 'Завершен'),
        (STATUS_CANCELLED, 'Отменен'),
    )

    user = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    total_amount = models.FloatField(default=0)
    shipping_address = models.CharField(max_length=500, blank=True, default='')
    comment = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return f"Order #{self.pk} ({self.get_status_display()})"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    thermostat = models.ForeignKey(Thermostat, related_name='order_items', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.FloatField()

    @property
    def subtotal(self):
        return float(self.price_at_purchase) * int(self.quantity)


class ThermostatComment(models.Model):
    thermostat = models.ForeignKey(Thermostat, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='thermostat_comments', on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    rating = models.PositiveIntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.text[:20]}"
