from behave import given, when, then
from src.temperatur.temperatur import omvandla_f_till_c
from src.temperatur.temperatur import omvandla_c_till_f


@given(u'att jag har temperaturen {temp_f:d} Fahrenheit')
def step_att_jag_har_temperatur_fahrenheit(context, temp_f):
    context.f = temp_f


@when(u'jag omvandlar till Celsius')
def step_jag_omvandlar_till_celsius(context):
    context.result = omvandla_f_till_c(context.f)


@then(u'ska svaret bli {expected:d} Celsius')
def step_ska_svaret_bli_celsius(context, expected):
    assert context.result == expected


@given(u'att jag har temperaturen {temp_c:d} Celsius')
def step_att_jag_har_temperatur_celsius(context, temp_c):
    context.c = temp_c


@when(u'jag omvandlar till Fahrenheit')
def step_jag_omvandlar_till_fahrenheit(context):
    context.result = omvandla_c_till_f(context.c)


@then(u'ska svaret bli {expected:d} Fahrenheit')
def step_ska_svaret_bli_fahrenheit(context, expected):
    assert context.result == expected
