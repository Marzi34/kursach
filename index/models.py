from django.db import models
from django.forms import ImageField
from users.models import CustomUser, Agent, Client


class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('house', 'Дом'),
        ('apartment', 'Квартира'),
        ('commercial', 'Коммерчиская'),
    ]
    CONDITION_CHOICES = [
        ('new', 'Новая'),
        ('good', 'Хорошая'),
        ('needs_renovation', 'Нуждается в реновации'),
    ]
    title = models.CharField(max_length=144)
    description = models.TextField()
    address = models.CharField(max_length=144)
    type = models.CharField(max_length=144, choices=PROPERTY_TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField(null=False)
    rooms = models.IntegerField(null=False)
    condition = models.CharField(max_length=144, choices=CONDITION_CHOICES)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True, related_name='properties')

    def __str__(self):
        return f"Property(price={self.price}, size={self.size})"


class Query(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Рассматриваемый'),
        ('processed', 'В процессе'),
        ('rejected', 'Отказано')
    ]
    query_date = models.DateField()
    status = models.CharField(max_length=144, choices=STATUS_CHOICES)
    message = models.TextField(null=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')