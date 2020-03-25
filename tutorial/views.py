from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.http import HttpResponse, HttpResponseRedirect

from mptt.exceptions import InvalidMove
from mptt.forms import MoveNodeForm

from tutorial.models import Genre
from tutorial.forms import GenreForm

# Create your views here.
def show_genres(request):
    return render(request,"tutorial/genres.html", {'genres': Genre.objects.all()})

def thanks_page(request):
    return HttpResponse("Thank you!")

def move_genre(request,genre_pk):
    genre = get_object_or_404(Genre, pk=genre_pk)

    if request.method == "POST":
        form = MoveNodeForm(genre,request.POST)

        if form.is_valid():
            try:
                genre = form.save()
                return render(request,"tutorial/genres.html", {'genres': Genre.objects.all()})

            except InvalidMove:
                pass
    else:
        form = MoveNodeForm(genre)

    return render('tutorial/move_genre.html', {
        'form': form,
        'genre': genre,
        'genre_tree': Genre.objects.all()
    })

class GenreFormView(FormView):
    template_name = 'tutorial/genre_form.html'
    form_class = GenreForm
    success_url = '/tutorial/thanks/'
