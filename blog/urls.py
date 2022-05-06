from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # views de postagens
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<str:post>/',
        views.post_detail,
        name='post_detail'),
]