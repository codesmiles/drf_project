from django.db import models
from django.utils import timezone
from accounts.models import User


class Transaction(models.Model):
    id = models.UUIDField(primary_key=True)
    tx_ref = models.CharField(max_length=250,blank=True,null=True)
    flw_ref = models.CharField(max_length=250, null=True, blank=True)
    amount = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=3, null=True, blank=True)
    app_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=250,blank=True, null=True)
    payment_type = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    merchant_fee = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    narration = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_transaction")

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return self.tx_ref