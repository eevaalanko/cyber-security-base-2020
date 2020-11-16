from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account, Message


@login_required
def deleteView(request):
    m = Message.objects.get(pk=request.POST.get('id'))
    m.delete()   # FLAW 2
    return redirect('/')


@csrf_exempt
@transaction.atomic
@login_required
def sendMessageView(request):
    print('sending message: ', request)
    sender = User.objects.get(username=request.user)
    receiver = User.objects.get(username=request.POST.get('receiver'))
    content = request.POST.get('content')
    newMessage = Message.objects.create(sender=sender, receiver=receiver, content=content)
    newMessage.save()

    return redirect('/')


@login_required
def homePageView(request):
    print('wuhuuu  ')
    user = User.objects.get(username=request.user)
    users = User.objects.filter(is_staff=False).exclude(username=user.username)
    print('users: ', users)
    messages = Message.objects.all()
    print('messages: ', messages)
    accounts = Account.objects.exclude(user_id=request.user.id)
    return render(request, 'pages/index.html', {'accounts': accounts, 'users': users, 'messages': messages, })
