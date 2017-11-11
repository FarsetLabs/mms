from rest_framework.test import APIClient

def before_feature(context, feature):
    context.resources = {}

def before_scenario(context, scenario):
    context.client = APIClient()
