from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    class Meta:
        name = 'Menu'
        name_plural = 'Menu Items'

    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    booking_date = models.DateTimeField()

    class Meta:
        name = 'Booking'
        name_plural = 'Booking Records'

    def __str__(self) -> str:
        return f'{self.name} for {self.number} guests on {self.booking_date}'
