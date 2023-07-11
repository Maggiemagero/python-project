from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def menu(request):
    return render(request,"menu.html")


def service(request):
    return render(request,"service.html")

def booking(request):
    return render(request,"booking.html")


def team(request):
    return render(request,"team.html")


def testimonial(request):
    return render(request,"testimonial.html")

