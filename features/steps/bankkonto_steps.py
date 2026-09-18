from behave import given, when, then
from src.bankkonto.bankkonto import BankAccount


@when(u'när jag skapar ett nytt konto för kunden {customer_name}')
def step_skapa_nytt_konto_for_kund(context, customer_name):
    context.konto = BankAccount(customer_name)


@then(u'ska startsaldot vara {start_sum:d} kr')
def step_ska_startsaldot_vara_noll(context, start_sum):
    saldo = context.konto.get_amount()
    assert saldo == start_sum


@given(u'att {customer_name} har ett konto med saldo {saldo_before:d} kr')
def step_ett_konto_har_saldo(context, customer_name, saldo_before):
    context.konto = BankAccount(customer_name, saldo_before)


@when(u'när han sätter in {amount_deposit:d} kr')
def step_insattning_pa_kontot(context, amount_deposit):
    context.konto.deposit(amount_deposit)


@then(u'ska saldot vara {amount_after:d} kr')
def step_ska_saldot_vara(context, amount_after):
    saldo = context.konto.get_amount()
    assert saldo == amount_after


@when(u'när han gör ett uttag på {withdraw_amount:d} kr')
def step_uttag_kr(context, withdraw_amount):
    context.konto.withdraw(withdraw_amount)
