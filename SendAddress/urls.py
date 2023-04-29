from django.contrib import admin
from django.urls import path
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MedHelp API",
      default_version='v1',
      description="Yordamga muhtojlardan tushgan so'rovlarni markazga yetkazuvchi loyiha uchun web-API",
      contact=openapi.Contact("Abdulhamid Egamberdiyev, <1997abdulhamid@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yordam/', MijozAPIView.as_view()),
    path('ochirish/<int:pk>/', MijozOchir.as_view()),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('', HomeView.as_view(), name='hammasi'),
]

