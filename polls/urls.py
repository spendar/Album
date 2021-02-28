from django.urls import path
from . import views

app_name = 'polls'

urlpatterns=[
    # path('', views.index, name='index'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.result, name='result'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]