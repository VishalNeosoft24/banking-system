from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    mobile_number = models.CharField(max_length=15, unique=True, help_text="Enter a valid mobile number")
    address = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.mobile_number})"


class Account(models.Model):
    ACCOUNT_TYPES = [
        ('Savings', 'Savings Account'),
        ('Current', 'Current Account'),
        ('Fixed Deposit', 'Fixed Deposit Account'),
    ]

    branch_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=18, unique=True, editable=False, default=uuid.uuid4)
    ifsc_code = models.CharField(max_length=11)
    bank_address = models.TextField()
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    def save(self, *args, **kwargs):
        if not self.account_number:
            last_account = Account.objects.order_by("-id").first()
            last_number = int(last_account.account_number) if last_account else 100000000000000000
            self.account_number = str(last_number + 1)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Account {self.account_number} - {self.account_type} at {self.branch_name}"


class UserAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accounts")
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="owner") 

    def __str__(self):
        return f"{self.user.username}'s Account: {self.account.account_number}"
