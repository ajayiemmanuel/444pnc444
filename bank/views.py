from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import CreateUserForm, CustomerForm, RedeemcardForm

from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.



def about(request):
    context = {}
    return render (request, "bank/about.html", context)


def reset(request):
    context = {}
    return render (request, "bank/reset.html", context)

@login_required (login_url = "login")
def apply_fixed(request):
    user = request.user

    fixed = user.fixed_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        depositplan = request.POST.get('depositplan')
        currency = request.POST.get('currency')
        amount = request.POST.get('amount')
        remark = request.POST.get('remark')
        attachment = request.POST.get('attachment')
        status = request.POST.get('status')
        time = request.POST.get('time')


        fixed, created = Fixed.objects.get_or_create(
            user=user,
            name=name,
            depositplan=depositplan,
            currency=currency,
            amount=amount,
            remark=remark,
            attachment=attachment,
            status=status,
            time=time
            )
        
        return redirect('pin')

    context = {'fixed':fixed} 
    return render (request, "bank/apply-fixed.html", context)

@login_required (login_url = "login")
def apply_loan(request):
    context = {}
    return render (request, "bank/apply-loan.html", context)


@login_required (login_url = "login")
def automatic_methods(request):
    context = {}
    return render (request, "bank/automatic-methods.html", context)


@login_required (login_url = "login")
def calculator(request):
    context = {}
    return render (request, "bank/calculator.html", context)


@login_required (login_url = "login")
def change_password(request):

    return render (request, "bank/change-password.html")



@login_required (login_url = "login")
def closedticket(request):
    context = {}
    return render (request, "bank/closedticket.html", context)

def contact(request):
    context = {}
    return render (request, "bank/contact.html", context)


@login_required (login_url = "login")
def create_ticket(request):
    user = request.user

    ticket = user.ticket_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        attachment = request.POST.get('attachment')
        status = request.POST.get('status')
        time = request.POST.get('time')


        ticket, created = Ticket.objects.get_or_create(
            user=user,
            name=name,
            subject=subject,
            message=message,
            attachment=attachment,
            status=status,
            time=time
            )
        
        return redirect('myticket')

    context = {'ticket':ticket} 
    return render (request, "bank/create-ticket.html", context)


@login_required (login_url = "login")
def card(request):
    context = {}
    return render (request, "bank/card.html", context)


@login_required (login_url = "login")
def dashboard(request):
    user = request.user

    transfer = Transfer.objects.filter(user=user)
    wiretransfer = Wiretransfer.objects.filter(user=user)
    banktransfer = Banktransfer.objects.filter(user=user)

    context = {'transfer':transfer, 'wiretransfer':wiretransfer, 'banktransfer' :banktransfer}
    return render (request, "bank/dashboard.html", context)


@login_required (login_url = "login")
def dps_schemes(request):
    context = {}
    return render (request, "bank/dps-schemes.html", context)


@login_required (login_url = "login")
def edit(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "bank/edit.html", context)

@login_required (login_url = "login")
def exchange_money(request):
    context = {}
    return render (request, "bank/exchange-money.html", context)

def faq(request):
    context = {}
    return render (request, "bank/faq.html", context)

def history(request):
    user = request.user

    fixed = Fixed.objects.filter(user=user)


    context = {'fixed':fixed}
    return render (request, "bank/history.html", context)

def index(request):
    context = {}
    return render (request, "bank/index.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('dashboard')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "bank/login.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')


@login_required (login_url = "login")
def manual_methods(request):
    context = {}
    return render (request, "bank/manual-methods.html", context)


@login_required (login_url = "login")
def manual_withdraw(request):
    user = request.user

    banktransfer = user.banktransfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        bankname = request.POST.get('bankname')
        accountnumber = request.POST.get('accountnumber')
        accountname = request.POST.get('accountname')
        currency = request.POST.get('currency')
        note = request.POST.get('note')
        charge = request.POST.get('charge')
        amount = request.POST.get('amount')
        time = request.POST.get('time')


        banktransfer, created = Banktransfer.objects.get_or_create(
            user=user,
            name=name,
            bankname=bankname,
            accountnumber=accountnumber,
            accountname=accountname,
            currency=currency,
            note=note,
            charge=charge,
            amount=amount,
            time=time
            )
        
        return redirect('pin')

    context = {'banktransfer':banktransfer}   
    return render (request, "bank/manual-withdraw.html", context)


@login_required (login_url = "login")
def my_loans(request):
    context = {}
    return render (request, "bank/my-loans.html", context)

@login_required (login_url = "login")
def myticket(request):
    user = request.user

    ticket = Ticket.objects.filter(user=user)

    context = {'ticket':ticket}
    return render (request, "bank/myticket.html", context)



@login_required (login_url = "login")
def payment_request(request):
    context = {}
    return render (request, "bank/payment-request.html", context)


@login_required (login_url = "login")
def payment_request(request):
    context = {}
    return render (request, "bank/payment-request.html", context)

def pin(request):
    context = {}
    return render (request, "bank/pin.html", context)
    
def plans(request):
    context = {}
    return render (request, "bank/plans.html", context)

def privacy_policy(request):
    context = {}
    return render (request, "bank/privacy-policy.html", context)



@login_required (login_url = "login")
def profile(request):
    context = {}
    return render (request, "bank/profile.html", context)



@login_required (login_url = "login")
def redeem_gift_cards(request):
    redeemcard = request.user.redeemcard
    form = RedeemcardForm (instance = redeemcard)

    if request.method == 'POST':
        form = RedeemcardForm (request.POST, request.FILES, instance = redeemcard)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "bank/redeem-gift-cards.html", context)


@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "bank/register.html", context)



@login_required (login_url = "login")
def send_money(request):
    user = request.user

    transfer = user.transfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        accountnumber = request.POST.get('accountnumber')
        currency = request.POST.get('currency')
        amount = request.POST.get('amount')        
        note = request.POST.get('note')
        date = request.POST.get('date')
        charge = request.POST.get('charge')
        status = request.POST.get('status')


        transfer, created = Transfer.objects.get_or_create(
            user=user,
            name=name,
            accountnumber=accountnumber,
            currency=currency,
            amount=amount,
            note=note,
            date=date,
            charge=charge,
            status=status
            )
        
        return redirect('pin')

    context = {'transfer':transfer} 
    return render (request, "bank/send-money.html", context)


def services(request):
    context = {}
    return render (request, "bank/services.html", context)


def terms_condition(request):
    context = {}
    return render (request, "bank/terms-condition.html", context)

@login_required (login_url = "login")
def transactions_report(request):
    user = request.user

    transfer = Transfer.objects.filter(user=user)
    wiretransfer = Wiretransfer.objects.filter(user=user)
    banktransfer = Banktransfer.objects.filter(user=user)

    context = {'transfer':transfer, 'wiretransfer':wiretransfer, 'banktransfer' :banktransfer}
    return render (request, "bank/transactions-report.html", context)


@login_required (login_url = "login")
def wire_transfer(request):
    user = request.user

    wiretransfer = user.wiretransfer_set.all()

    if request.method == 'POST':
        data = request.POST
        name = request.POST.getlist('name')
        bankname = request.POST.get('bankname')
        country = request.POST.get('country')
        swiftcode = request.POST.get('swiftcode')
        accountnumber = request.POST.get('accountnumber')
        accountname = request.POST.get('accountname')
        currency = request.POST.get('currency')
        note = request.POST.get('note')
        charge = request.POST.get('charge')
        amount = request.POST.get('amount')
        time = request.POST.get('time')


        wiretransfer, created = Wiretransfer.objects.get_or_create(
            user=user,
            name=name,
            bankname=bankname,
            country=country,
            swiftcode=swiftcode,
            accountnumber=accountnumber,
            accountname=accountname,
            currency=currency,
            note=note,
            charge=charge,
            amount=amount,
            time=time
            )
        
        return redirect('pin')

    context = {'wiretransfer':wiretransfer}   
    return render (request, "bank/wire-transfer.html", context)



