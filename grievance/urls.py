from django.contrib import admin
from django.urls import path
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import check_file

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
    path('login/', views.student_login, name='login'),
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
     path('contact', views.indexcontact),
     # Add this line to the urlpatterns
    path('admingrievanceview', views.admingrievanceview, name='admingrievanceview'),
    path('adminresolution/', views.admin_resolution_view, name='admin_resolution'),
    path('appealform/', views.appeal_form, name='appealform'), # Add this line for the appeal form4
    



    path('facultyhome/', views.fhome, name='facultyhome'), 
    path('facultylogin/', views.facultylog, name='facultylogin'), 
    path('faclog/', views.faculty_login, name='faclog'),

     path('facultyhome/events', views.events, name='events'),

path('eventsview/', views.events_view, name='events_view'),  # For viewing events (update the path to match 'eventsview')
 path('appealresolution/', views.appeal_resolution_view, name='appeal_resolution'),
 path('check-file/', check_file, name='check_file'),

 path('myprofile/', views.profile, name='myprofile'),  # Note the trailing slash

   path('myappeals/', views.my_appeals, name='my_appeals'),
    # path('login/forget/',views. change_password, name='forget_password'),
    path('login/forget/', views.openforget, name='forget'),
path('login/forget/changepass/', views.change_password, name='change_password'),


path('facultylogin/facforgetpassword/', views.facopenforget, name='forget'),
path('facultylogin/facforgetpassword/facchangepass/', views.fac_change_password, name='fac_change_password'),
# path('assignedgrievance/', views.assigned_grievance, name='assigned_grievance'),

path('facultyhome/assignedgrievance/', views.assigned_grievance, name='assigned_grievance'),

path('facultyresolution/', views.facresolution, name='facultyresolution'),


#  path('facultyresolution/', views.facresolution, name='facultyresolution'),  # Note the trailing slash
path('facultyresolution/<int:grievance_id>/', views.facresolution, name='submit_faculty_resolution'),

 path('', views.index, name='index'),

 path('facultylogout/', views.faculty_logout, name='facultylogout'),  # Faculty logout URL

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)