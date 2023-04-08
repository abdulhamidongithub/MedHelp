from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('yordam/', MijozAPIView.as_view()),
    path('', HomeView.as_view()),
]
