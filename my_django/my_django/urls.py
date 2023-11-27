from django.contrib import admin
from django.urls import path
from helloworld.views import hello_world  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),  # 追加
]

