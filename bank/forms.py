from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, SetPasswordForm, PasswordResetForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.models import User


class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']

class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

class CustomerForm (ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'name', 'verify']


class DepositForm (ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'
        exclude = ['user']
        

class LoanForm (ModelForm):
    class Meta:
        model = Loan
        fields = '__all__'
        exclude = ['user']

class TransferForm (ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'
        exclude = ['user']

class TicketForm (ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['user']

class FixedForm (ModelForm):
    class Meta:
        model = Fixed
        fields = '__all__'
        exclude = ['user']

class WiretransferForm (ModelForm):
    class Meta:
        model = Wiretransfer
        fields = '__all__'
        exclude = ['user']

class BanktransferForm (ModelForm):
    class Meta:
        model = Banktransfer
        fields = '__all__'
        exclude = ['user']

class RedeemcardForm (ModelForm):
    class Meta:
        model = Redeemcard
        fields = '__all__'
        exclude = ['user', 'name']

class ReportForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']

class AccountnumberForm (ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        exclude = ['user']

