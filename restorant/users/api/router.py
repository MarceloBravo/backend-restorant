from rest_framework.routers import DefaultRouter
from users.api.views import UsersApiViewSet

router_user = DefaultRouter()
router_user.register(prefix='users', basename='users', viewset= UsersApiViewSet)
