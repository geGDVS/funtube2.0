from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "app"
urlpatterns = [
    path("", views.home, name="home"),
]
urlpatterns += staticfiles_urlpatterns()
