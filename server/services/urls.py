from django.urls import path 

from . import views


urlpatterns = [
    path('specs', views.SpecsView.as_view(), name='specs'),
    path('publish/', views.PublishView.as_view(), name='publish'),
]