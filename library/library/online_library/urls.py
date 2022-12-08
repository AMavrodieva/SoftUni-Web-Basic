from django.urls import path, include

from library.online_library.views import index, add_book, edit_book, details_book, show_profile, edit_profile, \
    delete_profile, delete_book

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', include([
        path('', details_book, name='details book'),
        path('delete/', delete_book, name='delete book'),
    ])),
    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
]
