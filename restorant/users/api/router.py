
from django.url import path
from rest_framework.routers import DefaultRouter
from users.api.views import UsersApiViewSet, UserView

router_user = DefaultRouter()
router_user.register(prefix='users', basename='users', viewset= UsersApiViewSet)

urlpatterns = [
    path('auth/me/', UserView.as_view())
]
