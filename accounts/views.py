from django.shortcuts import render
from django.contrib import messages
from .forms import RegistrationForm
from .models import Account

def register(request):
    context = {}
    form = RegistrationForm()
    context.update({"form": form})
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        context["form"] = form
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            phone_number = form.cleaned_data["phone_number"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
        else:
            message = messages.error(request, form.errors)
            context.update({"messages":message})
        print("Is bound:", form.is_bound)
        print("Errors:", form.errors.as_json())
    else:
        form = RegistrationForm()
    
    return render(request, "accounts/register.html", context)


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return 