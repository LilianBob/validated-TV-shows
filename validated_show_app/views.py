from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)
def new_show(request):
    return render(request, 'create.html')
def back(request):
    return redirect("/shows")
def create(request):
    errors = Show.objects.validate(request.POST)
    if len(errors) >0:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        if 'release_date' not in request.POST:
            request.POST.get['release_date'] = '' 
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date= request.POST['release_date'],
            description=request.POST['description'],
        )
    
    return redirect('/shows')
def show(request, show_id):
    show_select = Show.objects.get(id=show_id)
    context = {
        'show': show_select
    }
    return render(request, 'show.html', context)
def edit(request, show_id):
    show_select = Show.objects.get(id=show_id)
    context = {
        'show': show_select
    }
    return render(request, 'edit.html', context)
def update(request, show_id):
    errors = Show.objects.validate(request.POST)
    if len(errors) >0:
        for (key, value) in errors.items():
            messages.error(request, value)
        return redirect(f'/edit/{ show_id }')
    else:
        show_update = Show.objects.get(id=show_id)
        show_update.title = request.POST['title']
        show_update.release_date = request.POST['release_date']
        show_update.network = request.POST['network']
        show_update.description = request.POST['description']
        show_update.save()
        messages.success(request, "Show successfully updated")
        return redirect(f'/show/{ show_id }')
def delete(request, show_id):
    d = Show.objects.get(id=show_id)
    d.delete()
    return redirect('/shows')
