from . import views
from django.urls import path

from .views import CreateCategoryAPIView

urlpatterns = [
    path("categories/", CreateCategoryAPIView.as_view()),
    ]