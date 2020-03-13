from django.urls import path;
from . import views ;
urlpatterns = [path('airline/create', views.createorupdateairline, name='airline creation and update'),
               path('airline/<int:id>/delete', views.deleteairline, name='airline deletion'),
               path('airline', views.getairlines, name='all airline'),
               path('airline/<int:id>', views.getsingleairline, name=' single airline'),
               path('user/create', views.createorupdateuser, name= 'user creation')]