from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Member

class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing members to be viewed or edited.
    """
    queryset = Member.objects.all().order_by('-first_joined_date')
    serializer_class = MemberSerializer
