from multiprocessing import context

from behave.api.pending_step import StepNotImplementedError
from behave import given, when, then
from src.lager.lager import Stock

@given(u'att jag har ett lager')
def step_jag_har_ett_lager(context):
    context.lager = Stock()


@given(u'att lagersaldo för bananer = {amount:d}')
def step_lagersaldo_bananer(context, amount):
    context.lager.increase_quantity("bananer", amount)


@when(u'jag lägger till {amount:d} bananer')
def step_jag_lagger_till_bananer(context, amount):
    context.lager.increase_quantity("bananer", amount)


@then(u'så ska lagersaldot vara {amount:d} bananer')
def step_lagersaldot_ska_vara(context, amount):
    product = context.lager.get_product("bananer")
    assert product.amount == amount, (
        f"Förväntade lagersaldo {amount}, och fick {product.amount}"
    )


@when(u'jag tar bort {amount:d} bananer')
def step_jag_tar_bort_bananer(context, amount):
    context.lager.decrease_quantity("bananer", amount)