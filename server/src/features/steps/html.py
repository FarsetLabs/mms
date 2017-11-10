from behave import *

@then(u'the response will not be empty')
def step_impl(context):
    context.test.assertTrue(len(context.response.content) > 0)

