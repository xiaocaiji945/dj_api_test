from django.urls import path

from . import views

app_name = 'interface'
urlpatterns = [
    # /interface
    path('', views.index, name='index'),
    # /interface/5/
    path('<int:tag_id>/', views.detail, name='detail'),
    # /interface/5/results/
    path('<int:tag_id>/results/', views.results, name='results'),
    # /interface/5/vote
    path('<int:tag_id>/vote/', views.vote, name='vote'),
]