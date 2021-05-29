from django.shortcuts import render, redirect
from .models import Show

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
    if request.method== "POST":
        Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date= request.POST['release_date'],
        description=request.POST['description'],
        )
    if 'release_date' not in request.POST:
        request.POST.get['release_date'] = '' or None  
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
    show_update = Show.objects.get(id=show_id)
    show_update.title = request.POST['title']
    show_update.release_date = request.POST['release_date']
    show_update.network = request.POST['network']
    show_update.description = request.POST['description']
    show_update.save()
    return redirect(f'/edit/{ show_id }')
def delete(request, show_id):
    d = Show.objects.get(id=show_id)
    d.delete()
    return redirect('/shows')
