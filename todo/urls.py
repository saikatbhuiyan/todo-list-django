from django.urls import path
from .views import home,about, delete, not_done, done, edit

urlpatterns = [
  path('', home, name='home'),
  path('about/', about, name='about'),
  path('delete/<list_id>', delete, name='delete'),
  path('done/<list_id>', done, name='done'),
  path('not_done/<list_id>', not_done, name='not_done'),
  path('edit/<list_id>', edit, name='edit'),
]
