from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('admin/',admin.site.urls),
    path('vic/',views.vic),
    path('finalsfdsbfzdf/',views.submit, name='final'),
    path('',views.home),

]