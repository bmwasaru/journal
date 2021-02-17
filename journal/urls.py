from django.urls import path, include

from rest_framework_nested import routers

from .views import AccountViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/account/login', LoginView.as_view(), name='login'),
    path('api/v1/account/logout', LogoutView.as_view(), name='logout'),
]
