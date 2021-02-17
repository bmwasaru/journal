from django.urls import path, include

from rest_framework_nested import routers

from .views import AccountViewSet, LoginView, LogoutView, PostViewSet, AccountPostsViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'posts', PostViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(accounts_router.urls)),
    path('api/v1/account/login', LoginView.as_view(), name='login'),
    path('api/v1/account/logout', LogoutView.as_view(), name='logout'),
]
