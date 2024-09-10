from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from wsgiapi.serializers import HumanAndFriendsSerializer
from basedata.models import Human


class HumanViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Human.objects.all().prefetch_related('friends')
    serializer_class = HumanAndFriendsSerializer
