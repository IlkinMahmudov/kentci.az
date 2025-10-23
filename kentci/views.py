from django.shortcuts import render, redirect
from .models import UserProfile

def login_view(request):
    if request.method == "POST":
        user_name = request.POST.get("user_name")
        email = request.POST.get("email")
        profile_image = request.FILES.get("profile_image")

        user, created = UserProfile.objects.get_or_create(email=email)
        user.user_name = user_name
        if profile_image:
            user.profile_image = profile_image
        user.save()

        request.session["user_id"] = user.id
        return redirect("index")

    return render(request, "login.html")


def index_view(request):
    user_id = request.session.get("user_id")
    user = UserProfile.objects.get(id=user_id) if user_id else None
    return render(request, "index.html", {"user": user})
