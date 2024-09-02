"""
URL configuration for grievance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.open),
    path('stdreg', views.registeropen),
    path('adminreg', views.adreg),
    path('sample', views.samp),
    path('shome', views.shome, name='shome'),  # Add this line for student home
    path('dashboard', views.student_dashboard, name='dashboard'),  # Add this for student dashboard
    path('about', views.indexabout),
    path('facreg', views.facultyreg),
    path('login', views.student_login, name='login'),
    path('registration', views.register), #registration details to login
    path('logout', views.logout, name='logout'),  # Add this for logout
    path('addcomplaint', views.addcomp),
    path('studenthome', views.stdhome),
    path('addcomplaints', views.complaint),
]
