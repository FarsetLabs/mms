from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    """Member within this management system.

    The Member model represents an individual member of the organization/body
    that this system manages.
    """

    first_joined_date = models.DateTimeField('date first joined')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
