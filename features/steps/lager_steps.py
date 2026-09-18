from behave import given, when, then
from src.lager.lager import Stock


@given(u'att jag har ett lager')
def step_jag_har_ett_lager(context):
    context.lager = Stock()


@given(u'att lagersaldo för {item} är {amount:d} st')
def step_lagersaldo_bananer(context, item, amount):
    context.lager.increase_quantity(item, amount)


@when(u'jag lägger till {amount:d} st {item}')
def step_jag_lagger_till_bananer(context, amount, item):
    context.lager.increase_quantity(item, amount)


@then(u'ska lagersaldot vara {amount:d} st {item}')
def step_lagersaldot_ska_vara(context, amount, item):
    product = context.lager.get_product(item)
    assert product.amount == amount


@when(u'jag tar bort {amount:d} st {item}')
def step_jag_tar_bort_bananer(context, amount, item):
    context.lager.decrease_quantity(item, amount)
