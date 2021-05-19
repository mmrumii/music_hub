from django.urls import path
from . import views

app_name = 'music'


urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),

    #registration
    path('register', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    path('<pk>', views.DetailView.as_view(), name='details'),

    # /music/album/add/
    path('album/add', views.AlbumCreate.as_view(), name='album-add'),

    # /music/album/edit/<album_id>
    path('album/edit/<pk>', views.AlbumUpdate.as_view(), name='album-update'),

    # /music/album/delete/<album_id>
    path('album/<pk>/delete', views.AlbumDelete.as_view(), name='album-delete'),

]

