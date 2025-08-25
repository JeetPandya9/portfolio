from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Technology, BlogPost, ContactMessage

def home(request):
    if request.method == "GET":
        projects = Project.objects.all()[:3]  # Get the latest 3 projects by [:3]
        return render(request, 'home.html', {"projects": projects})

def about(request):
    
    return render(request, 'about.html')

def projects(request):
    if request.method == "GET":
        projects = Project.objects.all()
        return render(request, 'projects.html', {"projects": projects})

def contact(request):
    if request.method == "POST":
        # process form data here (example)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # ✅ Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        # You can save to DB, send email, etc.
        return render(request, "contact.html", {"success": True})
    else:
        return render(request, "contact.html")  # ✅ must return template for GET

def blog(request):
    if request.method == "GET":
        posts = BlogPost.objects.all()
        return render(request, 'blog.html', {"posts": posts})
