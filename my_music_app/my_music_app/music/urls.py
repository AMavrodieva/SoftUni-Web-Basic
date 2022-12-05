from django.urls import path

from my_music_app.music.views import delete_profile, add_album, index, detail_album, edit_album, delete_album, \
    detail_profile, add_profile

urlpatterns = [
    path('', index, name='index'),
    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', detail_album, name='detail album'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    # path('profile/add/', add_profile, name='add profile'),
    path('profile/details/', detail_profile, name='detail profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]