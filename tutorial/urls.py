from django.urls import re_path
from tutorial.views import show_genres, thanks_page, move_genre, GenreFormView

urlpatterns = [
    re_path(r'^genres/$',show_genres),
    re_path(r'^form/$',GenreFormView.as_view()),
    re_path(r'^thanks/$',thanks_page),
    re_path(r'^(?P<genre_pk>\d+)/move',move_genre),
]
