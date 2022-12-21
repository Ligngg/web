from django.shortcuts import render , redirect
from .models import Movie
from django.http import HttpResponse
from .forms import MovieForm

# Create your views here.

def index(request):

    movie=Movie.objects.all()
    con={
        'movie_list':movie
    }
    return render(request,'index.html',con)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movies':movie})


def add(request):
    if request.method=='POST':
        name2 =request.POST.get('name1')
        descp2 = request.POST.get('descp1')
        year2 = request.POST.get('year1')
        img2 = request.FILES['img1']
        movie=Movie(name=name2,descp=descp2,year=year2,img=img2)
        movie.save()
        return redirect('/')

    return render(request,'add.html')

def update(request,id):
    moviee=Movie.objects.get(id=id)
    form1=MovieForm(request.POST or None, request.FILES,instance=moviee)
    if form1.is_valid():
        form1.save()
        return redirect('/')
    return render(request,'edit.html',{'form2':form1,'mov':moviee})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')