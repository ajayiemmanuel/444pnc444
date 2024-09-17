from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('dashboard/', views.dashboard, name = "dashboard"),
    path ('about/', views.about, name = "about"),
    path ('reset/', views.reset, name = "reset"),
    path ('apply_fixed/', views.apply_fixed, name = "apply-fixed"),
    path ('apply_loan/', views.apply_loan, name = "apply-loan"),
    path ('automatic_methods/', views.automatic_methods, name = "automatic-methods"),
    path ('calculator/', views.calculator, name = "calculator"),
    path ('change_password/', views.change_password, name = "change-password"),
    path ('closedticket/', views.closedticket, name = "closedticket"),
    path ('contact/', views.contact, name = "contact"),
    path ('create_ticket/', views.create_ticket, name = "create-ticket"),
    path ('card/', views.card, name = "card"),
    path ('dps_schemes/', views.dps_schemes, name = "dps-schemes"),
    path ('edit/', views.edit, name = "edit"),
    path ('exchange_money/', views.exchange_money, name = "exchange-money"),
    path ('faq/', views.faq, name = "faq"),
    path ('history/', views.history, name = "history"),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('manual_methods/', views.manual_methods, name = "manual-methods"),
    path ('manual_withdraw/', views.manual_withdraw, name = "manual-withdraw"),
    path ('my_loans/', views.my_loans, name = "my-loans"),
    path ('myticket/', views.myticket, name = "myticket"),
    path ('payment_request/', views.payment_request, name = "payment-request"),
    path ('plans/', views.plans, name = "plans"),
    path ('privacy_policy/', views.privacy_policy, name = "privacy-policy"),
    path ('profile/', views.profile, name = "profile"),
    path ('redeem_gift_cards/', views.redeem_gift_cards, name = "redeem-gift-cards"),
    path('register/', views.register, name='register'),
    path ('send_money/', views.send_money, name = "send-money"),
    path ('services/', views.services, name = "services"),
    path ('terms_condition/', views.terms_condition, name = "terms-condition"),
    path ('transactions_report/', views.transactions_report, name = "transactions-report"),
    path ('wire_transfer/', views.wire_transfer, name = "wire-transfer"),
    path ('pin/', views.pin, name = "pin"),

    ]