from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models


# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    verify = models.CharField (max_length = 200, null = True, default = "yes",)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)

    def __str__(self):
        return self.name

class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    dollar = models.CharField (max_length = 200,  null = True, default = "0",)
    notification_number = models.CharField (max_length = 200, default = "1",)
    notification_message = models.CharField (max_length = 200,)
    notification_time = models.CharField (max_length = 200, default = "19 hours ago",)



    def __str__(self):
        return self.name


class Loan (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200, blank = True,  null = True)
    active_loans = models.CharField (max_length = 200,  null = True)
    loan_id = models.CharField (max_length = 200)
    next_payment_date = models.CharField (max_length = 200)
    status = models.CharField (max_length = 200)
    amount_to_pay = models.CharField (max_length = 200)
    action = models.CharField (max_length = 200)



    def __str__(self):
        return self.name


status = (
    ('Pending...', 'Pending...'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),

    )

class Transfer (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    accountnumber = models.CharField (max_length = 200)
    currency = models.CharField (max_length = 200)
    amount = models.CharField (max_length = 200)
    note = models.TextField (max_length = 200)
    date = models.DateField(auto_now=True, editable = True)
    charge = models.CharField (max_length = 200, default = "-10",)
    status = models.CharField (max_length = 200, choices=status, default = "Pending...",)



    def __str__(self):
        return self.name

statu = (
    ('Pending...', 'Pending...'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),

    )

class Wiretransfer (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    bankname = models.CharField (max_length = 200)
    country = models.CharField (max_length = 200)
    swiftcode = models.TextField (max_length = 200)
    accountnumber = models.CharField (max_length = 200)
    accountname = models.CharField (max_length = 200)
    currency = models.CharField (max_length = 200)
    status = models.CharField (max_length = 200, choices=statu, default = "Pending...",)
    note = models.TextField (max_length = 200)
    charge = models.CharField (max_length = 200, default = "-10",)
    amount = models.CharField (max_length = 200)
    time = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

stat = (
    ('Pending...', 'Pending...'),
    ('Approved', 'Approved'),
    ('Declined', 'Declined'),

    )

class Banktransfer (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    bankname = models.CharField (max_length = 200)
    accountnumber = models.CharField (max_length = 200)
    accountname = models.CharField (max_length = 200)
    status = models.CharField (max_length = 200, choices=stat, default = "Pending...",)
    note = models.TextField (max_length = 200)
    currency = models.CharField (max_length = 200)
    charge = models.CharField (max_length = 200, default = "-10",)
    amount = models.CharField (max_length = 200)
    time = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

class Fixed (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    depositplan = models.CharField (max_length = 200)
    currency = models.CharField (max_length = 200)
    amount = models.CharField (max_length = 200)
    remark = models.TextField (max_length = 200)
    attachment = models.ImageField ( null = True, blank = True)
    status = models.CharField (max_length = 200, default = "Pending...",)
    time = models.DateField(auto_now=True)


    def __str__(self):
        return self.name

class Payment (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    receiver_account = models.CharField (max_length = 200, default = "",)
    amount = models.CharField (max_length = 200, default = "",)
    currency = models.CharField (max_length = 200, default = "USD",)
    description = models.CharField (max_length = 200, default = "",)


    def __str__(self):
        return self.name


class Redeemcard (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True, default="Amazon Gift Card")
    card_name = models.CharField (max_length = 200,  null = True, default="Amazon Gift Card")
    code = models.CharField (max_length = 200, default = "",)



    def __str__(self):
        return self.name


class Report (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    info = models.CharField (max_length = 200, default = "Welcome",)



    def __str__(self):
        return self.name

class Ticket (models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField (max_length = 200,  null = True)
    subject = models.CharField (max_length = 200,)
    message = models.TextField (max_length = 200,)
    attachment = models.ImageField ( null = True, blank = True)
    status = models.CharField (max_length = 200, default = "Pending...",)
    time = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Accountnumber (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account = models.CharField (max_length = 200, default = "Generating Account Number....",)



    def __str__(self):
        return self.name
