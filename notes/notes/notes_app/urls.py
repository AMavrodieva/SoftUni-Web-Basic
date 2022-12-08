from django.urls import path, include

from notes.notes_app.views import index, add_note, edit_note, delete_note, details_note, show_profile, delete_profile

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile', include([
        path('', show_profile, name='show profile'),
        path('delete/', delete_profile, name='delete profile')
    ])),
]
