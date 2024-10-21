from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.open),
    path('stdreg', views.registeropen),
    path('adminreg', views.adreg),
    path('sample', views.samp),
    path('shome', views.shome, name='shome'),
    path('dashboard', views.student_dashboard, name='dashboard'),
    path('about', views.indexabout),
    path('facreg', views.facultyreg),
    path('login', views.student_login, name='login'),
    path('registration', views.register),
    path('logout', views.logout, name='logout'),
    path('studenthome', views.stdhome),
    path('addcomplaint', views.addcomp, name='addcomplaint'),
    
    # Feedback related URLs
    path('feedbacktemplate/', views.stdfeedback, name="feedbacktemplate"),
    path('adminlogin', views.adminlogin, name="adminlogin"),
    path('ahome', views.ahome, name='adminhome'),
    path('ufeedbackform', views.ufeedbackform, name="ufeedbackform"),
    path('adminfeedbackview', views.admfeedbform, name="admfeedbform"),
    path('facultylogin', views.faculty_login, name='facultylogin'),
     path('contact', views.indexcontact),
     # Add this line to the urlpatterns
    path('admingrievanceview', views.admingrievanceview, name='admingrievanceview'),
    path('adminresolution/', views.admin_resolution_view, name='admin_resolution'),
    path('appealform/', views.appeal_form, name='appealform'),  # Add this line for the appeal form
]