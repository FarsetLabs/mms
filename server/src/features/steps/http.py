from behave import *

@when(r"I access the root URL")
def step_impl(context):
    context.response = context.test.client.get("/admin/", follow=True)
