from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # /sondages/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # /sondages/1/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /sondages/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]