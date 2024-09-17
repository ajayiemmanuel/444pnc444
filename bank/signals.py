from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)


def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)

def loan(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='loan')
        instance.groups.add(group)
        Loan.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(loan, sender=User)

def transaction(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transaction')
        instance.groups.add(group)
        Transaction.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transaction, sender=User)


def redeemcard(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='redeemcard')
        instance.groups.add(group)
        Redeemcard.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(redeemcard, sender=User)


def report(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='report')
        instance.groups.add(group)
        Report.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(report, sender=User)



def accountnumber(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='accountnumber')
        instance.groups.add(group)
        Accountnumber.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(accountnumber, sender=User)