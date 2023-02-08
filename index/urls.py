from django.urls import path
from .views import get_items, save, sort, register, rights
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register_view'),
    path('rights', rights),
    path('list', get_items),
    path('save', save),
    path('sorted', sort),
]
