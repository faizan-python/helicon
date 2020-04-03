from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import render_to_response


@require_http_methods(["POST"])
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return HttpResponse("Success")
    else:
        return HttpResponse("Username and Password do not match")
