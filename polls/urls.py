from django.urls import path

from . import views


app_name = 'polls'
urlpatterns = [
    # the 'name' value as called by the {% url %} template tag
    path('', views.index, name='index'),    # ex: /polls/
    path('<int:pk>/', views.detail, name='detail'),    # ex: /polls/5/
    path('<int:pk>/results/', views.results, name='results'),  # ex: /polls/5/results/
    path('<int:pk>/vote/', views.vote, name='vote'),   # ex: /polls/5/vote/
]

