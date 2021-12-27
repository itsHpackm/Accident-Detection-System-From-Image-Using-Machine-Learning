from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('accidentDetection', views.accidentDetection, name='accidentDetection'),
    path('makePred', views.get_image, name='accidentDetectionResults'),
    path('results', views.predResults, name='results'),
    path('loginPage', views.loginPage, name='loginPage'),
    path('signPage', views.signPage, name='signPage'),
    path('sign', views.sign, name='sign'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

]
