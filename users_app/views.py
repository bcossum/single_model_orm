from django.shortcuts import render, redirect
from .models import user

def index(request):
  context = {
    "all_the_users": user.objects.all()
  }
  return render(request, 'index.html', context)

def process(request):
  if request.method == "POST":
    user.objects.create(
      first_name=request.POST['first_name'], 
      last_name=request.POST['last_name'], 
      email_address=request.POST['email_address'], 
      age=request.POST['age'])
  return redirect('/')
    