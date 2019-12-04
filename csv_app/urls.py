from django.urls import path
from csv_app import views


urlpatterns = [
path('export/csv-simple-write/', views.csv_simple_write, name='csv_simple_write'),]
