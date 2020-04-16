from django.urls import path
from . import views
urlpatterns= [
    path('', views.index, name="index"),
    # example : /polls/
    path('<int:question_id>/', views.detail, name="detail"),
    # example : /polls/4/
    path('<int:question_id>/result/',views.results, name="results"),
    # example : /polls/4/result/
    path('<int:question_id>/vote/',views.vote,name="vote")
    # example : /polls/4/vote/
]