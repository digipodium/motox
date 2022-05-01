from pyexpat import model
from django.db import models
from decimal import Decimal

from payments import PurchasedItem
from payments.models import BasePayment

class Payment(BasePayment):

    def get_failure_url(self) -> str:
        return '/failure/'

    def get_success_url(self) -> str:
        return '/success/'

    def get_purchased_items(self):
        # Return items that will be included in this payment.
        yield PurchasedItem(
            name='The Hound of the Baskervilles',
            sku='BSKV',
            quantity=9,
            price=Decimal(10),
            currency='USD',
        )

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    team = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title
