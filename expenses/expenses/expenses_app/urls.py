from django.urls import path, include

from expenses.expenses_app.views import index, create_expenses, edit_expenses, delete_expenses, edit_profile, \
    delete_profile, show_profile

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_expenses, name='create expenses'),
    path('edit/<int:pk>/', edit_expenses, name='edit expenses'),
    path('delete/<int:pk>/', delete_expenses, name='delete expenses'),
    path('profile/', include([
        path('', show_profile, name='show profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ]))
]
