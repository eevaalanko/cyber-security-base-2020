from django.urls import path

from .views import homePageView, transferView, sendMessageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('transfer/', transferView, name='transfer'),
    path('sendMessage/', sendMessageView, name='sendMessage'),
]
