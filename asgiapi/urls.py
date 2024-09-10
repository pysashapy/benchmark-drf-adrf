from rest_framework import routers

from asgiapi import views

router = routers.DefaultRouter()
router.register(r'humans', views.HumanViewSet)

urlpatterns = router.urls
