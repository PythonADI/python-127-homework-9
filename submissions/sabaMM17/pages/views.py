from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "home.html")

def about_view(request):
    context = {"name": "Saba", "city": "Tbilisi", "age": 17}
    return render(request, "about.html", context)

def hobbies_view(request):
    hobbies = [
        {"name": "Basketball", "hours": 3},
        {"name": "Chess", "hours": 1},
        {"name": "Swimming", "hours": 2},
    ]
    return render(request, "hobbies.html", {"hobbies": hobbies})