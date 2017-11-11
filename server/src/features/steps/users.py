"""Steps and helpers relevant to MMS users

The included steps allow user creation and authentication during tests.
"""

from django.contrib.auth.models import User
from behave import *

def become_new_user(context, username, password, email):
    """Switch to a newly-created user.

    Switch the current user to a user created with the passed credentials.
    """

    u = User(username=username, email=email)
    u.set_password(password)
    u.save()

    c = context.client
    c.login(username=username, password=password)

# TODO: at present, only one authentication level
@given(r"I am an administrator")
def step_impl(context):
    become_new_user(
        context,
        'administrator',
        'pass123',
        'admin@example.net'
    )
