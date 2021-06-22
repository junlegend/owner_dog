from django.urls import path
from owner.views import OwnerView
from owner.views import DogView

urlpatterns = [
    path("", OwnerView.as_view()),
    path("/dog", DogView.as_view()),
]
