from adrf.viewsets import GenericViewSet
from adrf.mixins import RetrieveModelMixin

from asgiapi.serializers import HumanAndFriendsSerializer
from basedata.models import Human


class HumanViewSet(GenericViewSet, RetrieveModelMixin):
    queryset = Human.objects.all().prefetch_related('friends')
    serializer_class = HumanAndFriendsSerializer
