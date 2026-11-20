from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def about_view(request):
    context = {
        "name": "nina", 
        "city": "Tbilisi",
        "age": 17
        }
    return render(request, "about.html", context)

def hobbies_view(request):
    hobbies = [
        {"name": "Football", "hours": 4},
        {"name": "Chess", "hours": 2},
        {"name": "Guitar", "hours": 3},
    ]
    return render(request, "hobbies.html", {"hobbies": hobbies})