from rest_framework import routers

from wsgiapi import views

router = routers.DefaultRouter()
router.register(r'humans', views.HumanViewSet)

urlpatterns = router.urls
