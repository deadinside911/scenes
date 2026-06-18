from django.db import models

from decimal import Decimal

class ClubBank(models.Model):
    balance = models.DecimalField(decimal_places=2, max_digits=10)


class ReimbursementRequest(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)

