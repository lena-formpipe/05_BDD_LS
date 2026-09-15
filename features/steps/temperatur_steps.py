from behave import given, when, then
from behave.api.pending_step import StepNotImplementedError


@given(u': att jag har temperaturen 32 Fahrenheit')
def step_impl(context):
    context.f = 32
    context.constant = 32


@when(u': jag omvandlar till Celsius')
def step_impl(context):
    context.result = (context.f - context.constant)*5/9


@then(u': så ska svaret bli 0 Celsius')
def step_impl(context):
    assert context.result == 0


@given(u': att jag har temperaturen 100 Celsius')
def step_impl(context):
    context.c = 100
    context.constant = 32


@when(u': jag omvandlar till Fahrenheit')
def step_impl(context):
    context.result = (context.c * 9/5) + context.constant


@then(u': så ska svaret bli 212 Fahrenheit')
def step_impl(context):
    assert context.result == 212