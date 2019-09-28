from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import RegistrationForm
from django.http import JsonResponse
from django.views.generic import FormView
from .models import User

def index(request):
    return HttpResponseRedirect("Hello world")

class UserRegistrationView(FormView):
    form_class = RegistrationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        User.objects.create_user(username, password = password)

        res_data = {
            "error" : False,
            "message": "Success, please login"
        }

        return JsonResponse(res_data)

    def form_invalid(self, form):
        res_data = {
            "error": True,
            "errors": form.errors
        }
        return JsonResponse(res_data)
