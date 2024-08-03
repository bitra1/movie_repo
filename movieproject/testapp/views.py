from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import MovieModel
# Create your views here.
def index_info(request):
    return render(request,'testapp/index.html')

def list_movies_view(request):
    movie_list = MovieModel.objects.all()
    return render(request,'testapp/listmovies.html',{'movie_list':movie_list})

def add_movie_view(request):
    form = MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return index_info(request)
    return render(request,'testapp/addmovies.html',{'form':form})
