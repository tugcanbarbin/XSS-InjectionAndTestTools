from django.urls import path

from . import views
from .views import contact_result, homeView,searchbar,feed,BookDetailView,AddCommentView,comment,contact

urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:book_id>',views.book_by_id,name='book_by_id'),
    path('home', homeView, name='home'),
    path('searchbar',views.searchbar,name='searchbar'),
    path('feed', views.feed, name='feed'),
    path('bookdetail/<int:pk>',BookDetailView.as_view(),name="book_detail"),
    path('bookdetail/<int:pk>/add_comment/',AddCommentView.as_view(),name="add_comment"),
    path('contact',views.contact,name="contact"),
    path('contact_result',views.contact_result,name="contact_result"),
]
