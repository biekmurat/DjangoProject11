from django.shortcuts import render

def index(request):
    context = {}
    context["name"] = "Foodie"
    return render(request,"index.html",context)
