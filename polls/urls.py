from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

from pdf.views import GeneratePDF

app_name="polls"
urlpatterns = [
    path('list/', views.polls_list, name="list"),

    path('listAdmin/', views.polls_list_admin, name='listAdmin'),

    path('add/', views.add_poll, name="add"),

    path('edit/<int:poll_id>/',  views.edit_poll, name='edit_poll'),
    path('edit/<int:poll_id>/choice/add/',  views.add_choice, name='add_choice'),
    path('edit/choice/<int:choice_id>/', views.edit_choice, name="edit_choice"),
    path('delete/choice/<int:choice_id>/', views.delete_choice, name='choice_confirm_delete'),
    path('delete/poll/<int:poll_id>/', views.delete_poll, name='poll_confirm_delete'),

    path('details/<int:poll_id>/', views.polls_detail, name='detail'),
    path('details/<int:poll_id>/vote', views.poll_vote, name='vote'),


    path('pdf/', GeneratePDF.as_view(), name="pdf"),
]
