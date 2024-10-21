import re
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
from .models import Registers, Grievance, feedbackforms
from .forms import GrievanceForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
# from .forms import AppealForm
from django.contrib.auth import authenticate, login
from .models import Event
from .models import Appeal

def open(request):
    return render(request, 'index.html')

def registeropen(request):
    return render(request, 'stdreg.html')

def adreg(request):
    return render(request, 'adminreg.html')

def samp(request):
    return render(request, 'sample.html')

def shome(request):
    return render(request, 'studenthome.html')

def indexabout(request):
    return render(request, 'about.html')

def facultyreg(request):
    return render(request, 'facreg.html')


def facultylog(request):
    return render(request, 'facultylogin.html')

def log(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        # name = request.POST.get('name')
        department = request.POST.get('department')
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        phone_number=request.POST.get('phone_number')
         
        Registers.objects.create(name=request.user, department=department, mail=mail, password=password,phone_number=phone_number)
        # messages.success(request, "Registration successful!")
    return render(request, "index.html")

def student_login(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')

        try:
            user = Registers.objects.get(mail=mail, password=password)
            request.session['user_id'] = user.id
            # messages.success(request, "Login successful!")
            return redirect('shome')
        except Registers.DoesNotExist:
            messages.error(request, "Incorrect email or password")

    return render(request, 'login.html')

def student_dashboard(request):
    if 'user_id' in request.session:
        print(request.user)
        return render(request, 'student_dashboard.html')
    else:
        return redirect('login')

def logout(request):
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('index')

def addcomp(request):
    ow = request.session.get('user_id')
    person = Registers.objects.get(id=ow)
    
    if request.method == 'POST':
        # name and department values
        name = person.name
        department = request.POST['department']
        complaint_title = request.POST['complaint_title']
        type_of_grievance = request.POST['type_of_grievance']
        complaint_description = request.POST['complaint_description']
        
        # Save the grievance
        Grievance.objects.create(
            owner=person,
            name=name,
            department=department,
            complaint_title=complaint_title,
            type_of_grievance=type_of_grievance,
            complaint_description=complaint_description
        )
        
        # Add success message
        messages.success(request, "Grievance submitted successfully!")
        
        return redirect('shome')  # Replace with the appropriate redirect
    
    return render(request, 'addcomplaint.html')

def stdhome(request):
    return render(request, 'studenthome.html')

def stdfeedback(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message = request.POST["message"]
        feedbackforms.objects.create(fname=fname, lname=lname, email=email, message=message)
        # Set the flag to indicate successful submission
        request.session['submitted'] = True
        return redirect('feedbacktemplate')

    # Retrieve and clear the flag to avoid repeated alerts
    submitted = request.session.pop('submitted', False)
    return render(request, 'feedbacktemplate.html', {'submitted': submitted})

def adminlogin(request):
    if request.method == "POST":
        uname = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=uname, password=password)

        if user is not None and user.is_staff and user.is_superuser:
            auth.login(request, user)
            return redirect('adminhome')
        else:
            messages.error(request, 'Incorrect username or password')  # Set error message

    return render(request, 'adminlogin.html')

def ahome(request):
    return render(request, 'adminhome.html')

def ufeedbackform(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        message = request.POST["message"]
        feedbackforms.objects.create(fname=fname, lname=lname, email=email, message=message)
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('ufeedbackform')
    return render(request, 'feedbacktemplate.html')

# Admin Feedback Form Viewing
def admfeedbform(request):
    feedbacks = feedbackforms.objects.all()
    return render(request, 'adminfeedbackview.html', {'feedbacks': feedbacks})

def faculty_login(request):
    if request.method == 'POST':
        username = request.POST.get('mail')
        password = request.POST.get('password')
        user = Registers.objects.filter(mail=username, password=password).first()
        
        if user:
            request.session['faculty_email'] = user.mail
            return redirect('facultyhome')
        else:
            return render(request, 'facultylogin.html', {'error_message': 'Invalid email or password.'})

    return render(request, 'facultylogin.html')


def fhome(request):
    return render(request, 'facultyhome.html')


def indexcontact(request):
    return render(request, 'contact.html')
def admingrievanceview(request):
    grievances = Grievance.objects.all()
    faculties = Registers.objects.all()

    if request.method == 'POST':
        successfully_assigned = False  # Track if at least one assignment was made
        for grievance in grievances:
            faculty_email = request.POST.get(f'faculty_email_{grievance.id}')
            
            # Assign faculty only if no one is already assigned
            if faculty_email and grievance.assigned_to is None:
                try:
                    faculty = Registers.objects.filter(mail=faculty_email).first()
                    if faculty:
                        grievance.assigned_to = faculty  # Assign the faculty
                        grievance.save()  # Save the updated grievance
                        successfully_assigned = True
                    else:
                        messages.error(request, f"No faculty found with email: {faculty_email}")
                except Exception as e:
                    messages.error(request, f"Error assigning faculty: {str(e)}")
            elif grievance.assigned_to:
                messages.warning(request, f"Grievance '{grievance.complaint_title}' already has an assigned faculty.")

        if successfully_assigned:
            messages.success(request, "Faculties assigned successfully.")
        else:
            messages.info(request, "No new faculty was assigned.")

        return redirect('admingrievanceview')

    return render(request, 'admingrievanceview.html', {'grievances': grievances, 'faculties': faculties})

def admin_resolution_view(request):
    success_message = None  # Initialize success message

    if request.method == 'POST':
        grievance_id = request.POST.get('grievance_id')
        resolution = request.POST.get('resolution')

        # Fetch the grievance and check if the resolution already exists
        grievance = Grievance.objects.get(id=grievance_id)
        if not grievance.resolution:
            grievance.resolution = resolution
            grievance.save()

            # Set the success message to be passed to the template
            success_message = 'Resolution submitted successfully!'
        else:
            success_message = 'This grievance has already been resolved.'

        # Redirect to the same page after submission to clear form data
        return render(request, 'adminresolution.html', {'grievances': Grievance.objects.all(), 'success_message': success_message})

    # Fetch all grievances and render the page
    grievances = Grievance.objects.all()
    return render(request, 'adminresolution.html', {'grievances': grievances})

def appeal_form(request):
    ow = request.session.get('user_id')
    person = Registers.objects.get(id=ow)

    if request.method == 'POST':
        # Get form data from the request
        nature_of_appeal = request.POST.get('nature_of_appeal')
        details_of_appeal = request.POST.get('details_of_appeal')
        proposed_action = request.POST.get('proposed_action')
        supporting_documents = request.FILES.get('supporting_documents')
        signature = request.FILES.get('signature')

        # Create a new Appeal object and save it to the database
        appeal = Appeal(
            owner=person,
            nature_of_appeal=nature_of_appeal,
            details_of_appeal=details_of_appeal,
            proposed_action=proposed_action,
            supporting_documents=supporting_documents,
            signature=signature
        )
        appeal.save()

        # Add a success message and pass it to the template
        messages.success(request, 'Appeal submitted successfully.')
        return redirect('shome')

    return render(request, 'appealform.html')

def events(request):
    if request.method == 'POST':
        event_type = request.POST.get('event_type')
        description = request.POST.get('description')
        date = request.POST.get('date')

        # Validate that fields are filled out before saving
        if event_type and description and date:
            Event.objects.create(event_type=event_type, description=description, date=date)
            messages.success(request, 'Events added successfully!')  # Add success message
            return redirect('events')  # Redirect to the events page

    return render(request, 'events.html')  # Just render the template on GET

def events_view(request):
    events = Event.objects.all().order_by('date')  # Fetch all events ordered by date
    return render(request, 'eventsview.html', {'events': events})


def appeal_resolution_view(request):
    appeals = Appeal.objects.all()

    if request.method == 'POST':
        # Get the appeal ID and the submitted resolution from the POST request
        appeal_id = request.POST.get('appeal_id')
        appealresolution = request.POST.get('appealresolution')

        # Update the appeal with the resolution
        appeal = Appeal.objects.get(id=appeal_id)
        appeal.appealresolution = appealresolution
        appeal.save()

        # Redirect back to the appeal resolution page
        return redirect('appeal_resolution')

    return render(request, 'appealresolution.html', {'appeals': appeals})



import os
from django.http import HttpResponse
from django.conf import settings

def check_file(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'appeals/signatures/authen.png')
    if os.path.exists(file_path):
        return HttpResponse("File exists.")
    else:
        return HttpResponse("File does not exist.")


def profile(request):
    ow=request.session.get('user_id')
    person=Registers.objects.get(id=ow)
    
    grievances = Grievance.objects.filter(owner=person)
    return render(request, 'myprofile.html', {'grievances': grievances})


def my_appeals(request):
    # Fetch all appeals
    ow=request.session.get('user_id')
    person=Registers.objects.get(id=ow)
    
    appeals = Appeal.objects.filter(owner=person)
    return render(request, 'myappeals.html', {'appeals': appeals})

def openforget(request):
     return render(request, 'forgetpassword.html', {'step': '1'})

def change_password(request):
    if request.method == 'POST':
        step = request.POST.get('step', '1')  # Default to 1 if no step is provided

        if step == '1':
            phone_number = request.POST['num']

            # Validate phone number
            phone_pattern = re.compile(r'^\d{10}$')
            if not phone_pattern.match(phone_number):
                return render(request, 'forgetpassword.html', {
                    'error_message': 'Invalid phone number. Please enter a valid 10-digit phone number.',
                    'step': '1'
                })

            # Check if the phone number is associated with any account
            if not Registers.objects.filter(phone_number=phone_number).exists():
                return render(request, 'forgetpassword.html', {
                    'error_message': 'Phone number not found. Please check and try again.',
                    'step': '1'
                })

            # Proceed to the next step
            return render(request, 'forgetpassword.html', {
                'success_message': 'Phone number verified. Please enter your new password.',
                'step': '2',
                'num': phone_number
            })

        elif step == '2':
            phone_number = request.POST['num']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']

            if new_password != confirm_password:
                return render(request, 'forgetpassword.html', {
                    'error_message': 'Passwords do not match. Please try again.',
                    'step': '2',
                    'num': phone_number
                })

            if len(new_password) < 8 or not any(c.isnumeric() for c in new_password) or not any(c.isalpha() for c in new_password) or not any(not c.isalnum() for c in new_password):
                return render(request, 'forgetpassword.html', {
                    'error_message': 'Password must have a minimum of 8 characters, including at least one number, one letter, and one symbol.', 
                    'step': '2',
                    'num': phone_number
                })

            # Update the user's password
            user = Registers.objects.filter(phone_number=phone_number).first()

            user.password = new_password
            user.save()

            return render(request, 'login.html', {
                'success_message': 'Password has been reset successfully.'
            })

    return render(request, 'forgetpassword.html', {'step': '1'})


def facopenforget(request):
     return render(request, 'facforgetpassword.html', {'step': '1'})

def fac_change_password(request):
    if request.method == 'POST':
        step = request.POST.get('step', '1')  # Default to 1 if no step is provided

        if step == '1':
            phone_number = request.POST['num']

            # Validate phone number
            phone_pattern = re.compile(r'^\d{10}$')
            if not phone_pattern.match(phone_number):
                return render(request, 'facforgetpassword.html', {
                    'error_message': 'Invalid phone number. Please enter a valid 10-digit phone number.',
                    'step': '1'
                })

            # Check if the phone number is associated with any account
            if not Registers.objects.filter(phone_number=phone_number).exists():
                return render(request, 'facforgetpassword.html', {
                    'error_message': 'Phone number not found. Please check and try again.',
                    'step': '1'
                })

            # Proceed to the next step
            return render(request, 'facforgetpassword.html', {
                'success_message': 'Phone number verified. Please enter your new password.',
                'step': '2',
                'num': phone_number
            })

        elif step == '2':
            phone_number = request.POST['num']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']

            if new_password != confirm_password:
                return render(request, 'facforgetpassword.html', {
                    'error_message': 'Passwords do not match. Please try again.',
                    'step': '2',
                    'num': phone_number
                })

            if len(new_password) < 8 or not any(c.isnumeric() for c in new_password) or not any(c.isalpha() for c in new_password) or not any(not c.isalnum() for c in new_password):
                return render(request, 'facforgetpassword.html', {
                    'error_message': 'Password must have a minimum of 8 characters, including at least one number, one letter, and one symbol.', 
                    'step': '2',
                    'num': phone_number
                })

            # Update the user's password
            user = Registers.objects.filter(phone_number=phone_number).first()

            user.password = new_password
            user.save()

            return render(request, 'faclogin.html', {
                'success_message': 'Password has been reset successfully.'
            })

    return render(request, 'facforgetpassword.html', {'step': '1'})

def assigned_grievance(request):
    faculty_email = request.session.get('faculty_email')  # Get the email from session
    assigned_grievances = Grievance.objects.filter(assigned_to__mail=faculty_email)  # Filter grievances

    if request.method == 'POST':
        grievance_id = request.POST.get('grievance_id')
        resolution_text = request.POST.get('facultyresolution')

        # Fetch the grievance and update the resolution
        try:
            grievance = Grievance.objects.get(id=grievance_id)

            if grievance.facultyresolution:  # Check if resolution has already been provided
                messages.warning(request, 'Resolution has already been submitted for this grievance.')
                return redirect('assigned_grievance')

            grievance.facultyresolution = resolution_text
            grievance.save()

            # Add success message
            messages.success(request, 'Resolution added successfully!')

            # Redirect to faculty home after successful submission
            return redirect('facultyhome')
        except Grievance.DoesNotExist:
            # Handle the case where the grievance does not exist
            messages.error(request, 'Grievance does not exist.')
            return redirect('assigned_grievance')

    return render(request, 'assignedgrievance.html', {'assigned_grievances': assigned_grievances})
def facresolution(request):
    # Get the logged-in student's ID from the session
    student_id = request.session.get('user_id')
    
    # Fetch the student from the Registers model
    student = Registers.objects.get(id=student_id)
    
    # Retrieve grievances where the owner is the logged-in student
    grievances = Grievance.objects.filter(owner=student)
    
    # Render the grievances and pass them to the template
    return render(request, 'facultyresolution.html', {'grievances': grievances})


def index(request):
    return render(request, 'index.html')

def faculty_logout(request):
    # Clear the session to log out the faculty
    request.session.flush()
    
    # Redirect to the faculty login page
    return redirect('facultylogin')