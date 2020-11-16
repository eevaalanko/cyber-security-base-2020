from django.urls import path

from .views import homePageView, sendMessageView, deleteView

urlpatterns = [
    path('', homePageView, name='home'),
    path('sendMessage/', sendMessageView, name='sendMessage'),
    path('deleteMessage/', deleteView, name='deleteMessage'),
]
