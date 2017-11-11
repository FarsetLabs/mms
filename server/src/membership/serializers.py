from .models import Member
from rest_framework import serializers

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('first_joined_date', 'user_id')
