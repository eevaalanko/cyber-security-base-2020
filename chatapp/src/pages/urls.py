from django.urls import path

from .views import homePageView, sendMessageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sendMessage/', sendMessageView, name='sendMessage'),
]
