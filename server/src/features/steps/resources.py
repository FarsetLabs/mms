"""Steps and helpers relevant to resource testing.

The following routines simplify dealing with API testing of
a range of related resources in a consistent way.
"""

import json
from django.contrib.auth.models import User
from membership import models
from jsondiff import diff, symbols
from behave import *

resources = {
    'user': User,
    'member': models.Member
}
"""dict: Link test wording to actual instantiable models."""

def diff_contains(result):
    """Does a diff result show the first diff arg contains the second?"""

    # Make sure we are looking at a dictionary of diff results rather than
    # a placeholder list or empty object
    if result and not isinstance(result, list):
        for key, value in result.items():
            # If we have a dict, then we are dropping down a level of comparison
            if isinstance(value, dict):
                if not diff_contains(value):
                    return False
            # Otherwise, if we aren't simply missing comparable key/value pairs, this
            # isn't a 'contains'
            elif key != symbols.delete:
                return False

    # No objections found...
    return True

@given(r"a {resource} list")
def step_impl(context, resource):
    models = []

    # Keep track of these resources throughout the test
    if resource not in context.resources:
        context.resources[resource] = []

    for entry in context.table:
        fields = {}
        for field, value in entry.items():
            # If we are specifying an existing fixture from a similar table (say, Table A),
            # we can reference it in a column called 'field_name:resource_type'
            # with row entries being the row-index in Table A
            if ':' in field:
                field, subresource = field.split(':')
                ix = int(value)
                value = context.resources[subresource][ix]
            fields[field] = value

        # Instantiate and save a model
        new_model = resources[resource](**fields)
        new_model.save()

        models.append(new_model)

    context.resources[resource] += models

@when(r"I request a list of {resource}")
def step_impl(context, resource):
    c = context.client
    context.response = c.get('/{resource}/'.format(resource=resource))

@then(r"I should get a successful response")
def step_impl(context):
    assert context.response.status_code == 200

@then(r"the response should contain")
def step_impl(context):
    response_obj = context.response.json()
    comparison_obj = json.loads(context.text)

    result = diff(response_obj, comparison_obj)

    assert diff_contains(result)
