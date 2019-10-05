from django.urls import path
from . import views


app_name = 'apiRequestCount'

urlpatterns = [
    path('1/',
         views.CountView.as_view(), name='test-view1'),
    path('2/',
         views.CountView2.as_view(), name='test-view2'),
]